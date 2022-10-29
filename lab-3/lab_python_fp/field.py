def field(dist_list, *args):
    assert len(args) > 0
    yield [x for x in [
        {arg:dist_item[arg] for arg in
          args if arg in dist_item and dist_item[arg]} for dist_item in dist_list if bool(dist_item)
      ] if bool(x)]