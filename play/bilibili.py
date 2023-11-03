from bilibili_api import video


# 参数
BVID = "BV1pL411Y7d9"

# 获取视频信息
info = video.get_video_info(bvid=BVID)

# 假设这里获取 p1 的最新弹幕信息，需要取出 page_id，即每 p 都有自己的编号
page_id = info["pages"][0]["cid"]

# 然后开始获取弹幕
danmakus = video.get_danmaku(bvid=BVID)

# 打印出来！
for dm in danmakus:
    print(str(dm))