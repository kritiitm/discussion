import requests
import json

headers = {
    "Cookie" : "_bypass_cache=true; _gcl_au=1.1.710644445.1749808205; _ga=GA1.1.1723707373.1749808205; _fbp=fb.2.1749808204894.243129296343427391; _ga_5HTJMW67XK=GS2.1.s1749808204$o1$g0$t1749808211$j53$l0$h0; _ga_08NPRH5L4M=GS2.1.s1749808204$o1$g1$t1749808215$j49$l0$h0; _t=TvGCAzK8jDTF99FysRlF5w0N4d3Ht4ZV%2Bw%2BvRH0yA%2BZhSYqMJtSU15wqdmI9rCh%2BfGVaWaQZIVVnW%2BQwjtTd1hXeUdhzCC%2BvffMTGjOP8SJl1MfVF%2BsFq04Xs9bA9K7Gr8tBTV2PTdL1cEH7N%2F6lIqZSVJiySxPQ%2F1IxYT%2B40JzIFbtmkjuSS0Bb%2By%2FooF%2BD0NcZBE3YQUN1ntCMmA137im790SOYy0SELPtN7XZfEVoj%2FDsuXOQSyWhHr1JC9EVzgHwNhtYX5EqtJFXao37cvy2Luy7IHhx9OfYCdcI2w9Lj50lOEYWyVkfi5%2Bq3QFd--Tjl8Kulw66E1F9Dy--qwjPh1zltC8hW2Fa1xHhzw%3D%3D; _forum_session=FCImFKmcStibeVkC8ncgRHBMJjNOuYLeGzGCvVvedeSI%2BxBtTWfBaS2TaP0KmUzawTl55fmKtzIxkLKzzLrZrjZZTaJnQjMk%2BFCDnZi94DF9GKswBUthM9hrfR8Lh4OcOnidaQREx31A3G0RVhO08VmKtJNL4A2%2BDcTjI9JrlCaiJiT2cnclDUq664Zm6WSIbDtAZYpsSQ0LgV%2B9WQca0XapCRRXxbSIOx4aRJN2TI3gqtVJlajuLr%2FBNmbKSx9pwg7puRnNMv6lje4YFozHEfBVSVwn%2FwprFeu5WD3SeV0hysNqXjf%2BVX0D5lc4dIYOjuAwe8US8GImRA55NyjdplZXvZij4jHiXfnN4PSw%2Fz%2BdpqIwj5Yb3E04CQACdA%3D%3D--AHk2FWg0j1Rbq24u--i8hBgc6IU9QRE3KK%2BG7Zyw%3D%3D"
}


for i in range(1,7):
    response = requests.get(f"https://discourse.onlinedegree.iitm.ac.in/c/courses/tds-kb/34.json?page={i}",headers=headers)
    data = response.json()
    a = data["topic_list"]["topics"]
    with open(f"scraped_data{i}.json","w",encoding="utf-8") as f:
        json.dump(a,f,indent=2,ensure_ascii=False)


for i in range(0,1):
    response = requests.get(f"https://discourse.onlinedegree.iitm.ac.in/c/courses/tds-kb/34.json",headers=headers)
    data = response.json()
    a = data["topic_list"]["topics"]
    with open(f"scraped_data{i}.json","w",encoding="utf-8") as f:
        json.dump(a,f,indent=2,ensure_ascii=False)
