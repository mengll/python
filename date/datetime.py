# 获取当前时间戳的前n天 或后N天的时间戳
def get_timestamp_day(day,time_stmp =time.time()):
    day_temp = time.strftime("%Y-%m-%d",time.localtime(int(time_stmp)))
    day_temp = datetime.datetime.strptime(day_temp,"%Y-%m-%d")
    back = day_temp + datetime.timedelta(days=day)
    return int(back.timestamp())


# python 时间格式转化 设置时区
LOCAL_TIME_DELTA = datetime.timedelta(hours=8) 
def get_time(self, item):
        if item['create_ts']:
            create_ts = timestamp2string(item['create_ts'])
        else:
            start_time = item['created_at']
            if str(start_time).__contains__('.') and not str(start_time).__contains__('T'):
                create_ts = convert_datetime_to_timestamp(datetime.datetime.strptime(str(start_time),
                                                        "%Y-%m-%d %H:%M:%S.%f") + self.LOCAL_TIME_DELTA)
            elif str(start_time).__contains__('T'):
                create_ts = convert_datetime_to_timestamp(datetime.datetime.strptime(str(start_time),
                                                        "%Y-%m-%dT%H:%M:%S.%f") + self.LOCAL_TIME_DELTA)
            else:
                create_ts = convert_datetime_to_timestamp(
                    datetime.datetime.strptime(str(start_time), "%Y-%m-%d %H:%M:%S") + self.LOCAL_TIME_DELTA)

        return create_ts
