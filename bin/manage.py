import datetime
import os
import sys
import _thread
import threading
import traceback
import click
import logging
import logging.config
import pymysql

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

from conf import settings    # 导入环境变量
logging.config.dictConfig(settings.LOGGING_CONFIG)
pymysql.install_as_MySQLdb()

logger = logging.getLogger('uir')


@click.group()
def group_cmd():
    '''请输入指令'''
    pass


@group_cmd.command()
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@group_cmd.command()
@click.option('--host', default='0.0.0.0', help='server host')
@click.option('--port', default=8412, type=int, help='server port')
@click.option('--debug', default=True, type=bool, help='open flask debug mode')
def run_server(host, port, debug):
    """启动flask开发服务"""
    threading.currentThread().name = 'server'
    from libraryuir.web import create_app

    app = create_app()
    app.run(host, port, debug)


@group_cmd.command()
@click.option('--max_requests', default=500, type=int, help='max requests')
@click.option('--workers', default=5, type=int, help='worker cnt')
@click.option('--port', default=8413, type=int, help='port')
@click.option('--host', default='0.0.0.0', help='host')
def gunicorn_server(max_requests, workers, port, host):
    """以Gunicorn Application模式运行Service"""
    from libraryuir.web import create_app
    from gunicorn.app.base import Application
    # 删除命令行参数, 防止gunicorn Application重复解析命令行
    del sys.argv[1:]
    class FlaskApplication(Application):
        def init(self, parser, opts, args):
            gunicorn_options = {
                'bind': '{0}:{1}'.format(host, port),
                'workers': workers,
                'max_requests': max_requests,
                'timeout': 300,
                'access_log_format': '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" %(p)s %(T)s.%(D)6s "%(i)s" "%(o)s"',
            }
            # gunicorn_options.update(options)
            return gunicorn_options

        def load(self):
            return create_app()

    try:
        FlaskApplication().run()
    except Exception as e:
        logger.error(traceback.format_exc())
        sys.exit()


if __name__ == '__main__':
    group_cmd()