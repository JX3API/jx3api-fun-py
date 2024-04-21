import time

from jx3apifun import get_sync_handler

api = get_sync_handler()


def sync_test():
    result = api.data_active_calendar()
    print(f"data/active/calendar: {result}")
    time.sleep(0.5)

    result = api.data_active_list_calendar()
    print(f"data/active/list/calendar: {result}")
    time.sleep(0.5)

    result = api.data_active_celebrity()
    print(f"data/active/celebrity: {result}")
    time.sleep(0.5)

    result = api.data_exam_answer(match="古琴有几根弦")
    print(f"data/exam/answer: {result}")
    time.sleep(0.5)

    result = api.data_home_flower(server="长安城")
    print(f"data/home/flower: {result}")
    time.sleep(0.5)

    result = api.data_home_furniture(name="龙门香梦")
    print(f"data/home/furniture: {result}")
    time.sleep(0.5)

    result = api.data_home_travel(name="七秀")
    print(f"data/home/travel: {result}")
    time.sleep(0.5)

    result = api.data_news_allnews()
    print(f"data/news/allnews: {result}")
    time.sleep(0.5)

    result = api.data_news_announce()
    print(f"data/news/announce: {result}")
    time.sleep(0.5)

    result = api.data_school_toxic(name="冰心诀")
    print(f"data/school/toxic: {result}")
    time.sleep(0.5)

    result = api.data_server_master(name="长安城")
    print(f"data/server/master: {result}")
    time.sleep(0.5)

    result = api.data_server_check()
    print(f"data/server/check: {result}")
    time.sleep(0.5)

    result = api.data_server_status(server="长安城")
    print(f"data/server/status: {result}")
    time.sleep(0.5)

    result = api.data_save_detailed(server="唯我独尊", roleid="26468709")
    print(f"data/save/detailed: {result}")
    time.sleep(0.5)

    result = api.data_role_detailed(server="唯我独尊", name="夜温言@长安城")
    print(f"data/role/detailed: {result}")
    time.sleep(0.5)

    result = api.data_school_matrix(name="冰心诀")
    print(f"data/school/matrix: {result}")
    time.sleep(0.5)

    result = api.data_school_force(name="冰心诀")
    print(f"data/school/force: {result}")
    time.sleep(0.5)

    result = api.data_school_skills(name="冰心诀")
    print(f"data/school/skills: {result}")
    time.sleep(0.5)

    result = api.data_tieba_random(subclass="818")
    print(f"data/tieba/random: {result}")
    time.sleep(0.5)

    result = api.data_role_attribute(server="唯我独尊", name="夜温言@长安城")
    print(f"data/role/attribute: {result}")
    time.sleep(0.5)

    result = api.data_role_teamCdList(server="唯我独尊", name="夜温言@长安城")
    print(f"data/role/teamCdList: {result}")
    time.sleep(0.5)

    result = api.data_luck_adventure(server="唯我独尊", name="夜温言@长安城")
    print(f"data/luck/adventure: {result}")
    time.sleep(0.5)

    result = api.data_luck_statistical(server="长安城", name="阴阳两界")
    print(f"data/luck/statistical: {result}")
    time.sleep(0.5)

    result = api.data_luck_server_statistical(name="阴阳两界")
    print(f"data/luck/server/statistical: {result}")
    time.sleep(0.5)

    result = api.data_luck_collect(server="梦江南")
    print(f"data/luck/collect: {result}")
    time.sleep(0.5)

    result = api.data_role_achievement(
        server="唯我独尊", role="夜温言@长安城", name="阴阳两界"
    )
    print(f"data/role/achievement: {result}")
    time.sleep(0.5)

    result = api.data_match_recent(server="梦江南", name="有所依")
    print(f"data/match/recent: {result}")
    time.sleep(0.5)

    result = api.data_match_awesome()
    print(f"data/match/awesome: {result}")
    time.sleep(0.5)

    result = api.data_match_schools()
    print(f"data/match/schools: {result}")
    time.sleep(0.5)

    result = api.data_member_recruit(server="梦江南")
    print(f"data/member/recruit: {result}")
    time.sleep(0.5)

    result = api.data_member_teacher(server="梦江南")
    print(f"data/member/teacher: {result}")
    time.sleep(0.5)

    result = api.data_member_student(server="梦江南")
    print(f"data/member/student: {result}")
    time.sleep(0.5)

    result = api.data_server_sand(server="梦江南")
    print(f"data/server/sand: {result}")
    time.sleep(0.5)

    result = api.data_server_event()
    print(f"data/server/event: {result}")
    time.sleep(0.5)

    result = api.data_trade_demon()
    print(f"data/trade/demon: {result}")
    time.sleep(0.5)

    result = api.data_trade_record(name="狐金")
    print(f"data/trade/demon: {result}")
    time.sleep(0.5)

    result = api.data_tieba_item_records(name="狐金")
    print(f"data/tieba/item/records: {result}")
    time.sleep(0.5)

    result = api.data_valuables_statistical(server="梦江南", name="太一玄晶")
    print(f"data/valuables/statistical: {result}")
    time.sleep(0.5)

    result = api.data_valuables_server_statistical(name="太一玄晶")
    print(f"data/valuables/server/statistical: {result}")
    time.sleep(0.5)

    result = api.data_valuables_collect(server="梦江南")
    print(f"data/valuables/collect: {result}")
    time.sleep(0.5)

    result = api.data_server_antivice()
    print(f"data/server/antivice: {result}")
    time.sleep(0.5)

    result = api.data_rank_statistical(server="梦江南", table="个人", name="名士五十强")
    print(f"data/rank/statistical: {result}")
    time.sleep(0.5)

    result = api.data_rank_server_statistical(table="个人", name="名士五十强")
    print(f"data/rank/server/statistical: {result}")
    time.sleep(0.5)

    result = api.data_school_rank_statistical()
    print(f"data/school/rank/statistical: {result}")
    time.sleep(0.5)

    result = api.data_duowan_statistical()
    print(f"data/duowan/statistical: {result}")
    time.sleep(0.5)

    result = api.data_active_monster()
    print(f"data/active/monster: {result}")
    time.sleep(0.5)

    result = api.data_horse_event(server="梦江南")
    print(f"data/horse/event: {result}")
    time.sleep(0.5)

    result = api.data_watch_record(server="唯我独尊", name="风月的男宠")
    print(f"data/watch/record: {result}")
    time.sleep(0.5)

    result = api.data_watch_statistical(server="唯我独尊", name="真橙之心")
    print(f"data/watch/statistical: {result}")
    time.sleep(0.5)

    result = api.data_watch_collect(server="唯我独尊")
    print(f"data/watch/collect: {result}")
    time.sleep(0.5)

    result = api.data_watch_rank_statistical(
        server="唯我独尊", column="sender", this_time=1640285289, that_time=1640687624
    )
    print(f"data/watch/rank/statistical: {result}")
    time.sleep(0.5)

    result = api.data_role_monster(server="唯我独尊", name="夜温言@长安城")
    print(f"data/role/monster: {result}")
