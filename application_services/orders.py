from application_services.BaseApplicationResource import BaseApplicationResource
import database_services.RDBService as d_service


class OrderResource(BaseApplicationResource):

    def __init__(self):
        super().__init__()

    @classmethod
    def get_by_template(cls, template):
        res = d_service.find_by_template("demo_flask", "orders",
                                      template, None)
        return res


    @classmethod
    def get_by_order_id(cls, order_id):
        res = d_service.get_by_prefix("demo_flask", "orders",
                                      "order_id", order_id)
        return res

    @classmethod
    def get_by_customer_id(cls, customer_id):
        res = d_service.get_by_prefix("demo_flask", "orders",
                                      "customer_id", customer_id)
        return res


    @classmethod
    def create_by_order_id(cls, order_id):
        product_id = '3'
        price = '100'
        customer_id = '3'
        customer_name = 'Alex'
        date = '2021-10-11'
        res = d_service.create_order("demo_flask", "orders", order_id, product_id, price, customer_id, customer_name,date)
        return res





