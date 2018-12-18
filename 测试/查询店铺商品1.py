# -*- coding: utf-8 -*-
# @Time    : 2018-12-18 16:53
# @Author  : play4fun
# @File    : 查询店铺商品1.py
# @Software: PyCharm

"""
查询店铺商品1.py:

pdd.ddk.mall.goods.list.get
DdkMallGoodsListGet

"""


from ddk.api.rest.DdkMallGoodsListGet import DdkMallGoodsListGet
from ddk import appinfo
import traceback,json
from config import pdd_client_id,pdd_client_secret

def test1():
    req = DdkMallGoodsListGet()
    req.set_app_info(appinfo(pdd_client_id, secret=pdd_client_secret))
    #
    req.mall_id = 327071922
    try:
        resp = req.getResponse()
        print(resp)
        print('-' * 40)
        print(json.dumps(resp))

        # print(json.dumps(f, ensure_ascii=False))
    except Exception as e:
        print(e)
        print(traceback.format_exc())
    '''
    {
    "goods_info_list_response": {
        "total": 0,
        "goods_list": [
            {
                "category_name": "手机",
                "coupon_remain_quantity": null,
                "serv_pct": null,
                "promotion_rate": 10,
                "coupon_id": null,
                "lock_edit": null,
                "mall_id": 327071922,
                "share_desc": null,
                "mall_name": "白羽家",
                "coupon_price": 0,
                "rank": null,
                "desc_pct": null,
                "market_fee": 12,
                "goods_name": "磁吸数据线铝合金苹果安卓手机线快充磁力磁性充电线磁吸磁铁通用",
                "goods_eval_count": 0,
                "goods_id": 2205862698,
                "goods_gallery_urls": null,
                "goods_desc": null,
                "opt_name": "手机",
                "opt_ids": [
                    3138,
                    1555,
                    1543,
                    3146,
                    1546,
                    12,
                    3132,
                    1246,
                    223
                ],
                "goods_image_url": "http://t00img.yangkeduo.com/t11img/images/2018-07-20/c51d7e6d7ea88b5040159ad99dcb5ad5.jpeg",
                "is_valid": true,
                "min_group_price": 1250,
                "coupon_start_time": null,
                "coupon_discount": 0,
                "coupon_end_time": null,
                "avg_desc": null,
                "avg_serv": null,
                "avg_lgst": null,
                "sold_quantity": 24748,
                "cat_ids": null,
                "coupon_min_order_amount": 0,
                "goods_fact_price": 1250,
                "lgst_pct": null,
                "category_id": 1543,
                "goods_eval_score": 0,
                "cat_id": null,
                "coupon_total_quantity": null,
                "goods_rate": 10,
                "merchant_type": 1,
                "goods_mark_price": 2600,
                "qr_code_image_url": null,
                "goods_thumbnail_url": "http://t00img.yangkeduo.com/t02img/images/2018-07-14/9c231bba2c026435bae0cbeddd0f3100.jpeg",
                "broker": null,
                "opt_id": 1543,
                "sale_num_today": null,
                "sale_num24": 31,
                "min_normal_price": 1400,
                "has_coupon": false,
                "goods_mall_coupon_price": null,
                "mall_rate": 10,
                "goods_type": 1,
                "create_at": null,
                "mall_cps": 1
            },
            {
                "category_name": "手机",
                "coupon_remain_quantity": 100,
                "serv_pct": null,
                "promotion_rate": 10,
                "coupon_id": 370854822,
                "lock_edit": null,
                "mall_id": 327071922,
                "share_desc": null,
                "mall_name": "白羽家",
                "coupon_price": 300,
                "rank": null,
                "desc_pct": null,
                "market_fee": 44,
                "goods_name": "USB灯移动电源USB小夜灯床头台灯宿舍灯护眼USB灯",
                "goods_eval_count": 0,
                "goods_id": 4979630814,
                "goods_gallery_urls": null,
                "goods_desc": null,
                "opt_name": "手机",
                "opt_ids": [
                    3362,
                    2483,
                    3364,
                    2517,
                    1543,
                    1559,
                    1546,
                    12,
                    3149,
                    1246,
                    2478,
                    223
                ],
                "goods_image_url": "http://t00img.yangkeduo.com/goods/images/2018-12-16/690c972321f07917f9482bcb365249fa.jpeg",
                "is_valid": true,
                "min_group_price": 449,
                "coupon_start_time": 1545062400,
                "coupon_discount": 300,
                "coupon_end_time": 1545235199,
                "avg_desc": null,
                "avg_serv": null,
                "avg_lgst": null,
                "sold_quantity": 2071,
                "cat_ids": null,
                "coupon_min_order_amount": 300,
                "goods_fact_price": 449,
                "lgst_pct": null,
                "category_id": 1543,
                "goods_eval_score": 0,
                "cat_id": null,
                "coupon_total_quantity": 1000,
                "goods_rate": 10,
                "merchant_type": 1,
                "goods_mark_price": 5400,
                "qr_code_image_url": null,
                "goods_thumbnail_url": "http://t00img.yangkeduo.com/goods/images/2018-12-16/d11c3627319f49c7876dc31418243dcf.jpeg",
                "broker": null,
                "opt_id": 1543,
                "sale_num_today": null,
                "sale_num24": 950,
                "min_normal_price": 549,
                "has_coupon": true,
                "goods_mall_coupon_price": null,
                "mall_rate": 10,
                "goods_type": 1,
                "create_at": null,
                "mall_cps": 1
            },
            {
                "category_name": "手机",
                "coupon_remain_quantity": 50,
                "serv_pct": null,
                "promotion_rate": 10,
                "coupon_id": 369720612,
                "lock_edit": null,
                "mall_id": 327071922,
                "share_desc": null,
                "mall_name": "白羽家",
                "coupon_price": 300,
                "rank": null,
                "desc_pct": null,
                "market_fee": 59,
                "goods_name": "充电线收纳盒充电器数据线收纳包u盘耳机线收纳盒",
                "goods_eval_count": 0,
                "goods_id": 4791600618,
                "goods_gallery_urls": null,
                "goods_desc": null,
                "opt_name": "手机",
                "opt_ids": [
                    3362,
                    3363,
                    3364,
                    3365,
                    1543,
                    1545,
                    12,
                    3149,
                    2477,
                    1246,
                    223
                ],
                "goods_image_url": "",
                "is_valid": true,
                "min_group_price": 499,
                "coupon_start_time": 1544976000,
                "coupon_discount": 300,
                "coupon_end_time": 1545148799,
                "avg_desc": null,
                "avg_serv": null,
                "avg_lgst": null,
                "sold_quantity": 605,
                "cat_ids": null,
                "coupon_min_order_amount": 300,
                "goods_fact_price": 499,
                "lgst_pct": null,
                "category_id": 1543,
                "goods_eval_score": 0,
                "cat_id": null,
                "coupon_total_quantity": 1000,
                "goods_rate": 10,
                "merchant_type": 1,
                "goods_mark_price": 2500,
                "qr_code_image_url": null,
                "goods_thumbnail_url": "http://t00img.yangkeduo.com/goods/images/2018-12-08/d006bbd5ea2509536bd2ca0b37f32f01.jpeg",
                "broker": null,
                "opt_id": 1543,
                "sale_num_today": null,
                "sale_num24": 125,
                "min_normal_price": 599,
                "has_coupon": true,
                "goods_mall_coupon_price": null,
                "mall_rate": 10,
                "goods_type": 1,
                "create_at": null,
                "mall_cps": 1
            },
            {
                "category_name": "海淘",
                "coupon_remain_quantity": 50,
                "serv_pct": null,
                "promotion_rate": 10,
                "coupon_id": 368848962,
                "lock_edit": null,
                "mall_id": 327071922,
                "share_desc": null,
                "mall_name": "白羽家",
                "coupon_price": 300,
                "rank": null,
                "desc_pct": null,
                "market_fee": 81,
                "goods_name": "手机防水袋水下拍照触屏潜水游泳防水袋温泉防水袋通用款",
                "goods_eval_count": 0,
                "goods_id": 4810395645,
                "goods_gallery_urls": null,
                "goods_desc": null,
                "opt_name": "海淘",
                "opt_ids": [
                    482,
                    277,
                    295,
                    12,
                    223,
                    15,
                    479
                ],
                "goods_image_url": "",
                "is_valid": true,
                "min_group_price": 570,
                "coupon_start_time": 1544976000,
                "coupon_discount": 300,
                "coupon_end_time": 1545148799,
                "avg_desc": null,
                "avg_serv": null,
                "avg_lgst": null,
                "sold_quantity": 376,
                "cat_ids": null,
                "coupon_min_order_amount": 300,
                "goods_fact_price": 570,
                "lgst_pct": null,
                "category_id": 12,
                "goods_eval_score": 0,
                "cat_id": null,
                "coupon_total_quantity": 1000,
                "goods_rate": 10,
                "merchant_type": 1,
                "goods_mark_price": 1999,
                "qr_code_image_url": null,
                "goods_thumbnail_url": "http://t00img.yangkeduo.com/goods/images/2018-12-09/8db1c2671def8a2616bf05aad8653982.jpeg",
                "broker": null,
                "opt_id": 12,
                "sale_num_today": null,
                "sale_num24": 122,
                "min_normal_price": 670,
                "has_coupon": true,
                "goods_mall_coupon_price": null,
                "mall_rate": 10,
                "goods_type": 1,
                "create_at": null,
                "mall_cps": 1
            },
            {
                "category_name": "手机",
                "coupon_remain_quantity": 50,
                "serv_pct": null,
                "promotion_rate": 10,
                "coupon_id": 367245382,
                "lock_edit": null,
                "mall_id": 327071922,
                "share_desc": null,
                "mall_name": "白羽家",
                "coupon_price": 100,
                "rank": null,
                "desc_pct": null,
                "market_fee": 379,
                "goods_name": "【19.99元抢200件，抢完恢复24.99元】磁吸数据线车载快充苹果oppo华为type-c安卓vivo充电器线手机通用",
                "goods_eval_count": 0,
                "goods_id": 3354254431,
                "goods_gallery_urls": null,
                "goods_desc": null,
                "opt_name": "手机",
                "opt_ids": [
                    3138,
                    1555,
                    1543,
                    3146,
                    1546,
                    12,
                    3132,
                    1246,
                    223
                ],
                "goods_image_url": "http://t00img.yangkeduo.com/goods/images/2018-12-12/683ec30d8485f78aa30a014de3c681db.png",
                "is_valid": true,
                "min_group_price": 1999,
                "coupon_start_time": 1544889600,
                "coupon_discount": 100,
                "coupon_end_time": 1545148799,
                "avg_desc": null,
                "avg_serv": null,
                "avg_lgst": null,
                "sold_quantity": 311,
                "cat_ids": null,
                "coupon_min_order_amount": 100,
                "goods_fact_price": 1999,
                "lgst_pct": null,
                "category_id": 1543,
                "goods_eval_score": 0,
                "cat_id": null,
                "coupon_total_quantity": 100,
                "goods_rate": 10,
                "merchant_type": 1,
                "goods_mark_price": 3400,
                "qr_code_image_url": null,
                "goods_thumbnail_url": "http://t00img.yangkeduo.com/goods/images/2018-10-15/708992dd75138dd210aee31f682dbac4.jpeg",
                "broker": null,
                "opt_id": 1543,
                "sale_num_today": null,
                "sale_num24": 0,
                "min_normal_price": 2600,
                "has_coupon": true,
                "goods_mall_coupon_price": null,
                "mall_rate": 10,
                "goods_type": 1,
                "create_at": null,
                "mall_cps": 1
            },
            {
                "category_name": "手机",
                "coupon_remain_quantity": null,
                "serv_pct": null,
                "promotion_rate": 10,
                "coupon_id": null,
                "lock_edit": null,
                "mall_id": 327071922,
                "share_desc": null,
                "mall_name": "白羽家",
                "coupon_price": 0,
                "rank": null,
                "desc_pct": null,
                "market_fee": 7,
                "goods_name": "弯头数据线苹果67快充安卓Type-C铝合金充电线手机充电器线抖音款",
                "goods_eval_count": 0,
                "goods_id": 2190814663,
                "goods_gallery_urls": null,
                "goods_desc": null,
                "opt_name": "手机",
                "opt_ids": [
                    3138,
                    1555,
                    1543,
                    3146,
                    1546,
                    12,
                    3132,
                    1246,
                    223
                ],
                "goods_image_url": "http://t00img.yangkeduo.com/t05img/images/2018-07-14/db025ef4bb19649e37038898c9a2ed13.jpeg",
                "is_valid": true,
                "min_group_price": 744,
                "coupon_start_time": null,
                "coupon_discount": 0,
                "coupon_end_time": null,
                "avg_desc": null,
                "avg_serv": null,
                "avg_lgst": null,
                "sold_quantity": 25,
                "cat_ids": null,
                "coupon_min_order_amount": 0,
                "goods_fact_price": 744,
                "lgst_pct": null,
                "category_id": 1543,
                "goods_eval_score": 0,
                "cat_id": null,
                "coupon_total_quantity": null,
                "goods_rate": 10,
                "merchant_type": 1,
                "goods_mark_price": 2000,
                "qr_code_image_url": null,
                "goods_thumbnail_url": "http://t00img.yangkeduo.com/t01img/images/2018-07-14/7da751ee1a0be875fbde832e7afab69d.jpeg",
                "broker": null,
                "opt_id": 1543,
                "sale_num_today": null,
                "sale_num24": 0,
                "min_normal_price": 990,
                "has_coupon": false,
                "goods_mall_coupon_price": null,
                "mall_rate": 10,
                "goods_type": 1,
                "create_at": null,
                "mall_cps": 1
            },
            {
                "category_name": "手机",
                "coupon_remain_quantity": null,
                "serv_pct": null,
                "promotion_rate": 10,
                "coupon_id": null,
                "lock_edit": null,
                "mall_id": 327071922,
                "share_desc": null,
                "mall_name": "白羽家",
                "coupon_price": 0,
                "rank": null,
                "desc_pct": null,
                "market_fee": 24,
                "goods_name": "弯头苹果数据线二合一快充安卓充电线耳机转接头7p/8p/x一体接口",
                "goods_eval_count": 0,
                "goods_id": 3293377900,
                "goods_gallery_urls": null,
                "goods_desc": null,
                "opt_name": "手机",
                "opt_ids": [
                    3138,
                    1555,
                    1543,
                    3146,
                    1546,
                    12,
                    3132,
                    1246,
                    223
                ],
                "goods_image_url": "",
                "is_valid": true,
                "min_group_price": 2499,
                "coupon_start_time": null,
                "coupon_discount": 0,
                "coupon_end_time": null,
                "avg_desc": null,
                "avg_serv": null,
                "avg_lgst": null,
                "sold_quantity": 19,
                "cat_ids": null,
                "coupon_min_order_amount": 0,
                "goods_fact_price": 2499,
                "lgst_pct": null,
                "category_id": 1543,
                "goods_eval_score": 0,
                "cat_id": null,
                "coupon_total_quantity": null,
                "goods_rate": 10,
                "merchant_type": 1,
                "goods_mark_price": 2900,
                "qr_code_image_url": null,
                "goods_thumbnail_url": "http://t00img.yangkeduo.com/goods/images/2018-10-11/d17fc94e6468566381404ae9a1e9f361.jpeg",
                "broker": null,
                "opt_id": 1543,
                "sale_num_today": null,
                "sale_num24": 0,
                "min_normal_price": 2680,
                "has_coupon": false,
                "goods_mall_coupon_price": null,
                "mall_rate": 10,
                "goods_type": 1,
                "create_at": null,
                "mall_cps": 1
            },
            {
                "category_name": "手机",
                "coupon_remain_quantity": null,
                "serv_pct": null,
                "promotion_rate": 10,
                "coupon_id": null,
                "lock_edit": null,
                "mall_id": 327071922,
                "share_desc": null,
                "mall_name": "白羽家",
                "coupon_price": 0,
                "rank": null,
                "desc_pct": null,
                "market_fee": 359,
                "goods_name": "弯头数据线苹果oppo华为充电线vivo安卓快充线",
                "goods_eval_count": 0,
                "goods_id": 4373252800,
                "goods_gallery_urls": null,
                "goods_desc": null,
                "opt_name": "手机",
                "opt_ids": [
                    3138,
                    1555,
                    1543,
                    3146,
                    1546,
                    12,
                    3132,
                    1246,
                    223
                ],
                "goods_image_url": "http://t00img.yangkeduo.com/goods/images/2018-11-21/625bb4b0c44dc4bc4c735d9af693fc0a.jpeg",
                "is_valid": true,
                "min_group_price": 1199,
                "coupon_start_time": null,
                "coupon_discount": 0,
                "coupon_end_time": null,
                "avg_desc": null,
                "avg_serv": null,
                "avg_lgst": null,
                "sold_quantity": 12,
                "cat_ids": null,
                "coupon_min_order_amount": 0,
                "goods_fact_price": 1199,
                "lgst_pct": null,
                "category_id": 1543,
                "goods_eval_score": 0,
                "cat_id": null,
                "coupon_total_quantity": null,
                "goods_rate": 10,
                "merchant_type": 1,
                "goods_mark_price": 2499,
                "qr_code_image_url": null,
                "goods_thumbnail_url": "http://t00img.yangkeduo.com/goods/images/2018-11-28/ad6e5fe5349b9b94d8df2e0f15f84fcc.jpeg",
                "broker": null,
                "opt_id": 1543,
                "sale_num_today": null,
                "sale_num24": 0,
                "min_normal_price": 1299,
                "has_coupon": false,
                "goods_mall_coupon_price": null,
                "mall_rate": 10,
                "goods_type": 1,
                "create_at": null,
                "mall_cps": 1
            }
        ],
        "request_id": "15451234279400740"
    }
}
    '''

if __name__ == '__main__':
    test1()