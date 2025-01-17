__author__ = "Johannes Köster"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"


import os
import tempfile
from pathlib import Path
from snakemake.shell import shell
from snakemake_wrapper_utils.samtools import get_samtools_opts

samtools_opts = get_samtools_opts(snakemake)
extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

out_name, out_ext = os.path.splitext(snakemake.output[0])

with tempfile.TemporaryDirectory() as tmpdir:
    tmp_prefix = Path(tmpdir) / "samtools_fastq.sort_"

    shell(
        "samtools sort {samtools_opts} {extra} -T {tmp_prefix} {snakemake.input[0]} {log}"
    )
