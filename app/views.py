from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi
from flask_appbuilder import models, AppBuilder, expose, BaseView, has_access

from . import appbuilder, db

"""
    Create your Model based REST API::

    class MyModelApi(ModelRestApi):
        datamodel = SQLAInterface(MyModel)

    appbuilder.add_api(MyModelApi)


    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(
        MyModelView,
        "My View",
        icon="fa-folder-open-o",
        category="My Category",
        category_icon='fa-envelope'
    )
"""

"""
    Application wide 404 error handler
"""


@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )


db.create_all()

class Myview(BaseView):
    route_base = "/myview"


    @expose('/method1/<string:param1>')
    @has_access
    def method1(self,param1 ):
        return param1

    @expose('/method2/<string:param2>')
    def method2(self, param2):
        param = 'Hello %s' %(param2)
        return param

appbuilder.add_view_no_menu(Myview())


# class MyModelApi(ModelRestApi):
#     datamodel = SQLAInterface(MyModel)
#
#
# appbuilder.add_api(MyModelApi)
#
# # Create your Views::
#
# class MyModelView(ModelView):
#     datamodel = SQLAInterface(MyModel)
#
#
# # Next, register your Views::
#
#
# appbuilder.add_view(
#     MyModelView,
#     "My View",
#     icon="fa-folder-open-o",
#     category="My Category",
#     category_icon='fa-envelope'
# )
