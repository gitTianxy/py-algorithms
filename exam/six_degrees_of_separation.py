# encoding=utf-8
"""
LEVEL:
    primary
CONTEXT:
    “六度空间理论”非常有名, 大概的意思是: 1个人只需要通过6个中间人就可以和世界上任何1个人产生间接联系。
PROBLEM:
    假设拥有同样约数（不包括1）的数字互为“好友”.
    1) 从1~N中任意选取一个“合数”，求从它开始，要经历几层好友，才能和其他所有的数产生联系（所谓的“合数”是指“有除1以及自身以外的约数的自然数”）。
    2) 求从1~N中选取7个合数时，最多经过6层就可以与其他所有数产生联系的最小的N。
解:

"""
import random


class FriendsNode:
    def __init__(self, host, friends):
        self.host = host
        self.friends = friends


def find_longest_route(n, host):
    global nodes
    route_longest = []
    composites = get_all_friends(n)
    nodes = dict()
    for composite in composites:
        nodes[str(composite)] = get_all_friends(composite, composites)
    route_current = list(host)
    for f in nodes[str(host)]:
        pass


def append_route(route_curr, num):
    global nodes
    has_friends = False
    for i in range(0, len(route_curr)-1):
        if is_friend(num, route_curr[i]):
            has_friends = True
            break
    if not has_friends:
        route_curr.append(num)
        friends = nodes[str(num)]
        for f in friends:
            append_route(route_curr, f)
    else:
        return


def get_divisors(num):
    """
    get all divisors for num
    :param num:
    :return:
    """
    divisors = []
    for i in range(2, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def get_all_composites(n):
    """
    find out all composites for numbers within [0,n]
    :param n:
    :return:
    """
    composites = []
    for num in range(0, n + 1):
        is_composite = False
        for i in range(2, num):
            if num % i == 0:
                is_composite = True
        if is_composite:
            composites.append(num)
    return composites


def is_friend(host, guest):
    """
    judge whether guest is friend of host: whether they share divisor
    :param host:
    :param guest:
    :return:
    """
    host_divisor = get_divisors(host)
    guest_divisor = get_divisors(guest)
    for divisor in host_divisor:
        if divisor in guest_divisor:
            return True
    return False


def get_all_friends(host, collection):
    """
    get all friends for host within the collections
    :param host:
    :param collection:
    :return:
    """
    all_friends = []
    for p in collection:
        if is_friend(host, p):
            all_friends.append(p)
    return all_friends


if __name__ == '__main__':
    n = 20
    '''
    # 0. get all composite number
    composites = get_all_composites(n)
    for item in composites:
        print item
    # 1. pick out one host
    # host = random.choice(composites)
    host = [3, 9]
    print 'choose:', host


    # 2. pick out all not-friend
    not_friends = []
    for item in composites:
        if item[len(item) - 1] == host[len(host) - 1]:
            continue
        if is_friend(host, item):
            continue
        not_friends.append(item)
    # 3. pick out all friends of not-friend, respectively
    friendship_route = []
    friend_trace_route = []
    while len(not_friends) > 0:
        for not_friend in not_friends:
            friend_trace_route
            all_friends = get_all_friends(not_friend, composites)
            for friend in all_friends:
                if is_friend(host, friend):
                    not_friends.remove(not_friend)
                    friendship_route.append(list(host[len(host)-1], not_friend[len(not_friend)-1], friend[len(friend)-1]))
                    break
                else:
                    pass

    # 4a. if they share friends, process stop and store friendship-route

    # 4b. if there is no shared friend, do '3' again

    # 5. compare all friendship-route and pick out the longest one
    '''
