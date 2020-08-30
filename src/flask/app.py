#!/usr/bin/env python3
from pathlib import Path

def application(env, start_response):
    slurm_config = Path("/var/snap/slurm/common/etc/slurm/slurm.conf")
    if slurm_config.exists():
        slurm_config = slurm_config.read_text()
    else:
        slurm_config = ""
    start_response('200 OK', [('Content-Type','plain/text')])
    return [slurm_config.encode()]
