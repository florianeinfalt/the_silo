def all_reads():
    """Reload all read nodes in the compositing script"""
    import nuke
    for node in nuke.allNodes('Read'):
        node.knob('reload').execute()
