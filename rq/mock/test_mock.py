#coding=utf-8
import requests
import json

# url='https://test.weiyangpuhui.com/payBill/recharge.shtml'
# data={"id":"0",
#       "bankId":"BOC",
#       "bankName":"中国银行",
#       "payType":"3",
#       "money":"4.99",
#       "usrId":"85174",
#       "token":"b4d7ac821b1047ff93c7889c38b205cc"}
#
# res=requests.post(url=url,data=data)
# print(res.text)


from flask import Flask, request, jsonify, abort
import random

app = Flask(__name__) # 实例化⼀个Flask对象

@app.route("https://test.weiyangpuhui.com/payBill/recharge.shtml", methods=["POST"])

def reg():
      if not request.json or not 'usrId' in request.json or not 'money' in request.json:
            abort(404)
      res = [
                  {
                  "entity": "{\"appRetUrl\":\"https://test.weiyangpuhui.com/dist/result/rechargeResult/3e7cace0b8a64f07a1aa1f2af895189f\",\"order_id\":\"14201911100000002561\",\"order_no\":\"202003092237022708\",\"sequence_id\":\"2b39f957709ecea383a6cfe14f25fc02\",\"successed\":false,\"url\":\"https://testecas2.srbank.cn/ecpg/rtp3?orderid=14201911100000002561&srul=https%3A%2F%2Ftest.weiyangpuhui.com%2Fdist%2Fresult%2FrechargeResult%2F3e7cace0b8a64f07a1aa1f2af895189f&furl=https%3A%2F%2Ftest.weiyangpuhui.com%2Fdist%2Fresult%2FrechargeResult%2F3e7cace0b8a64f07a1aa1f2af895189f&fpurl=https%3A%2F%2Ftest.weiyangpuhui.com%2Faccount%2FmodifyTrandePassword.do\",\"uuid\":\"3e7cace0b8a64f07a1aa1f2af895189f\"}",
                  "code": 0,
                  "message": "成功",
                  "secced": "secced"
                   },

                  {
                  "entity": "{ }",
                  "code": 1,
                  "message": "失败，金额小于5",
                  "fail": "fail"

                  }

            ]
      return jsonify(random.choice(res))
      if __name__ == '__main__':
       app.run()