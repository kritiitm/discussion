### Post 35
**Post URL**: /t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/35
- **ID**: 587764
- **Author**: Andrew David (23f1002382)
- **Created At**: 2025-01-30T06:26:20.605Z
- **Content**:  
  I had set up the environment and dependencies and everything was working fine. When i tried to recreate it from scratch in a new codespace it broke. I fixed almost everything except this error
<pre><code class="lang-auto">@ANdIeCOOl ➜ /workspaces/TDS-Project-1 (main) $ crewai create crew b2b
Traceback (most recent call last):
  File "/home/codespace/.python/current/bin/crewai", line 5, in &lt;module&gt;
    from crewai.cli.cli import crewai
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/crewai/__init__.py", line 3, in &lt;module&gt;
    from crewai.agent import Agent
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/crewai/agent.py", line 7, in &lt;module&gt;
    from crewai.agents import CacheHandler
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/crewai/agents/__init__.py", line 2, in &lt;module&gt;
    from .parser import CrewAgentParser
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/crewai/agents/parser.py", line 6, in &lt;module&gt;
    from crewai.utilities import I18N
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/crewai/utilities/__init__.py", line 13, in &lt;module&gt;
    from .embedding_configurator import EmbeddingConfigurator
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/crewai/utilities/embedding_configurator.py", line 4, in &lt;module&gt;
    from chromadb import Documents, EmbeddingFunction, Embeddings
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/chromadb/__init__.py", line 6, in &lt;module&gt;
    from chromadb.auth.token_authn import TokenTransportHeader
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/chromadb/auth/token_authn/__init__.py", line 24, in &lt;module&gt;
    from chromadb.telemetry.opentelemetry import (
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/chromadb/telemetry/opentelemetry/__init__.py", line 13, in &lt;module&gt;
    from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/opentelemetry/exporter/otlp/proto/grpc/trace_exporter/__init__.py", line 25, in &lt;module&gt;
    from opentelemetry.exporter.otlp.proto.grpc.exporter import (  # noqa: F401
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/opentelemetry/exporter/otlp/proto/grpc/exporter.py", line 72, in &lt;module&gt;
    from opentelemetry.sdk.metrics.export import MetricsData
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/opentelemetry/sdk/metrics/__init__.py", line 16, in &lt;module&gt;
    from opentelemetry.sdk.metrics._internal import Meter, MeterProvider
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/__init__.py", line 56, in &lt;module&gt;
    from opentelemetry.sdk.metrics._internal.measurement_consumer import (
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/measurement_consumer.py", line 29, in &lt;module&gt;
    from opentelemetry.sdk.metrics._internal.metric_reader_storage import (
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/metric_reader_storage.py", line 26, in &lt;module&gt;
    from opentelemetry.sdk.metrics._internal._view_instrument_match import (
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/_view_instrument_match.py", line 22, in &lt;module&gt;
    from opentelemetry.sdk.metrics._internal.aggregation import (
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/aggregation.py", line 48, in &lt;module&gt;
    from opentelemetry.sdk.metrics._internal.exponential_histogram.mapping.exponent_mapping import (
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exponential_histogram/mapping/exponent_mapping.py", line 25, in &lt;module&gt;
    from opentelemetry.sdk.metrics._internal.exponential_histogram.mapping.ieee_754 import (
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exponential_histogram/mapping/ieee_754.py", line 15, in &lt;module&gt;
    from ctypes import c_double, c_uint64
  File "/usr/local/python/3.12.1/lib/python3.12/ctypes/__init__.py", line 8, in &lt;module&gt;
    from _ctypes import Union, Structure, Array
ImportError: /usr/local/python/3.12.1/lib/python3.12/lib-dynload/_ctypes.cpython-312-x86_64-linux-gnu.so: undefined symbol: ffi_type_uint32, version LIBFFI_BASE_7.0
</code></pre>
i updated the libffi package using sudo but while breaking something else can someone pls help me? <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/s.anand">@s.anand</a><br>
<br><br>
<br><br>
<br>
history of commands in new codespace
<pre><code class="lang-auto">    1  crewai --version
    2  pip install crewai crewai-tools
    3  python3 -c "import sqlite3; print(sqlite3.sqlite_version)"
    4  export PATH=/opt/conda/bin:$PATH
    5  export LD_LIBRARY_PATH=/opt/conda/lib:$LD_LIBRARY_PATH
    6  python3 -c "import sqlite3; print(sqlite3.sqlite_version)"
    7  crewai create crew &lt;project_name&gt;
    8  crewai create crew b2b
    9  history
</code></pre>
<br>
<br>
UPDATE: IT’s WORKING if you do this in order
<pre><code class="lang-auto">    1  python3 -c "import sqlite3; print(sqlite3.sqlite_version)"
    2  export PATH=/opt/conda/bin:$PATH
    3  export LD_LIBRARY_PATH=/opt/conda/lib:$LD_LIBRARY_PATH
    4  python3 -c "import sqlite3; print(sqlite3.sqlite_version)"
    5  pip install --no-cache-dir --force-reinstall typing_extensions pydantic crewai crewai-tools
    6  conda install -c conda-forge typing_extensions
    7  exec bash
    8  crewai create crew "Project 1 - LLM-based Automation Agent"
</code></pre>
Something about different environment conda and python can the instructors please help me understand it(resources ), so i can trouble shoot this later with better accuracy come precision
- **Reactions**: heart (1)
- **Post Number**: 35

