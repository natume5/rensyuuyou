def route(strat, end, *args):
    route_list = [strat]
    route_list += list(args)
    route_list += [end]
    route_str = "→".join(route_list)
    print(route_str)


strat = "東京"
end = "宮崎"
route(strat, end, "神戸", "長崎", "熊本")
