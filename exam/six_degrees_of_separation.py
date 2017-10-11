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


class Route:
    def __init__(self, route=[], is_finish=False):
        self.route = route
        self.is_finish = is_finish

    def __str__(self):
        return 'route: %s, is_finish: %s' % (self.route, self.is_finish)


def init_nodes(composites):
    """
    node: the data structure for storing the host-friends relation
    :param n:
    :return:
    """
    global nodes
    nodes = dict()
    for composite in composites:
        nodes[str(composite)] = get_all_friends(composite, composites)
    print '---- ALL NODES ----'
    for k, v in nodes.iteritems():
        print "%s: %s" % (k, v)


def get_route_set(host):
    global nodes
    route_set = []
    for f in nodes[str(host)]:
        route = Route()
        route.route = [host, f]
        route_set.append(route)
    append_route(route_set)
    print '---- ROUTE SET ----'
    for rt in route_set:
        print rt
    return route_set


def find_longest_route(composites, host):
    """
    corresponds to 'PROBLEM 1)'
    """
    # init nodes
    init_nodes(composites)
    # get route set
    route_set = get_route_set(host)
    # get longest route
    longest_route = []
    for rt in route_set:
        if len(longest_route) < len(rt.route):
            longest_route = rt.route
    return longest_route


def append_route(route_set):
    global nodes
    finish_count = 0
    for route in route_set:
        if route.is_finish:
            finish_count += 1
            continue
        tail = route.route[len(route.route) - 1]
        tail_friends = nodes[str(tail)]
        friend_count = 0
        new_routes = []
        for tf in tail_friends:
            i = 0
            appendable = True
            while i < len(route.route) - 1:
                if is_friend(tf, route.route[i]):
                    friend_count += 1
                    appendable = False
                    break
                i += 1
            if appendable:
                new_rt = list(route.route)
                new_rt.append(tf)
                new_routes.append(Route(new_rt, False))
        if friend_count == len(tail_friends):
            route.is_finish = True
        else:
            route_set.remove(route)
            route_set.extend(new_routes)
    if finish_count < len(route_set):
        append_route(route_set)


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
        if p == host:
            continue
        if is_friend(host, p):
            all_friends.append(p)
    return all_friends


if __name__ == '__main__':
    n = 20
    composites = get_all_composites(n)
    host = random.choice(composites)
    print '---- HOST ----'
    print host
    longest_rt = find_longest_route(composites, host)
    print '---- longest route:', longest_rt
