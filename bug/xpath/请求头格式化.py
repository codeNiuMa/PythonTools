

def fmt(s):
    p, q = 0, 1
    while q<len(s):
        k = s[p].replace(':', '')
        v = s[q]
        print('\''+k+'\''+':'+'\''+v+'\',')

        p+=1
        q = p+1


s =('''Accept:
text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding:
gzip, deflate, br
Accept-Language:
zh-CN,zh;q=0.9
Cache-Control:
max-age=0
Cookie:
lastCity=101020100; wd_guid=c3dd51a0-8b86-4b09-baad-a245815fa864; historyState=state; _bl_uid=anlXUhvLgz0a6835k2qkjwtasULO; collection_pop_window=1; __fid=133dfd4563650eef272feb61429677fb; __zp_seo_uuid__=66baa3c4-a5bc-4d84-b785-cb921905e079; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1697533622,1697599047,1697601713; __g=-; __l=r=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DvA6g63g2jUyGv9pAhVBuFZhrHFsbTzGWJSQ3Vs1bKNDmR64aA9IbdVmH5kdhHL5n%26wd%3D%26eqid%3Dcc23e0c500017ded00000006652f58ab&l=%2Fwww.zhipin.com%2Fshanghai%2F&s=1&g=&s=3&friend_source=0; boss_login_mode=wechat; wt2=DDn0Lt-StU8uCYFRsq5HTzRD18jarYPJJb2GDoueRgIA6t2SUGmuerCoDtt-PBhpJGScUTv_kjTM7zPek6jjOBQ~~; wbg=0; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1697606675; __c=1697601713; __a=72525633.1666921538.1697599047.1697601713.132.14.9.40; geek_zp_token=V1R9gkEeL60lhvVtRvxhoeKSyy7jvRwi0~; __zp_stoken__=0a14eAGRWDh5QUyhWR1thaEtaHklHAXQTRTR3eFtWSHFKYzBZbBlLASlvHkADL38hJmQHGDd%2BfRIlUAo8VV14J31Ddxp6aQg6KCBKc3MpbWpUA15BPyA5dRRVNDg9azB3ZF01Zy13fBhybHo%3D; SERVERID=606144fb348bc19e48aededaa626f54e|1697606728|1697606562
Referer:
https://www.zhipin.com/?ka=header-home-logo
Sec-Ch-Ua:
"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"
Sec-Ch-Ua-Mobile:
?0
Sec-Ch-Ua-Platform:
"Windows"
Sec-Fetch-Dest:
document
Sec-Fetch-Mode:
navigate
Sec-Fetch-Site:
same-origin
Sec-Fetch-User:
?1
Upgrade-Insecure-Requests:
1
User-Agent:
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36''').split('\n')

fmt(s)