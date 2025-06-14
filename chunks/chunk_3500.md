### Post 436
**Post URL**: /t/tds-official-project1-discrepencies/171141/436
- **ID**: 616862
- **Author**: Carlton D'Silva (carlton)
- **Created At**: 2025-04-08T06:29:24.100Z
- **Reply To**: Post 430 (Bharat Choudhary, 23f1000879)
- **Content**:  
  There is <strong>clearly</strong> <em>some difference</em> between both the applications. That is up to you to figure out. I can only tell whats wrong with yours. After building it and trying to run it this is the error we get. It fails to run as a result and we cannot evaluate it.
<pre><code class="lang-auto">Traceback (most recent call last):
  File "/usr/local/bin/uvicorn", line 8, in &lt;module&gt;
    sys.exit(main())
             ^^^^^^
  File "/usr/local/lib/python3.12/site-packages/click/core.py", line 1161, in __call__
    return self.main(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/click/core.py", line 1082, in main
    rv = self.invoke(ctx)
         ^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/click/core.py", line 1443, in invoke
    return ctx.invoke(self.callback, **ctx.params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/click/core.py", line 788, in invoke
    return __callback(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/uvicorn/main.py", line 412, in main
    run(
  File "/usr/local/lib/python3.12/site-packages/uvicorn/main.py", line 579, in run
    server.run()
  File "/usr/local/lib/python3.12/site-packages/uvicorn/server.py", line 66, in run
    return asyncio.run(self.serve(sockets=sockets))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/asyncio/runners.py", line 195, in run
    return runner.run(main)
           ^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/asyncio/runners.py", line 118, in run
    return self._loop.run_until_complete(task)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/asyncio/base_events.py", line 691, in run_until_complete
    return future.result()
           ^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/uvicorn/server.py", line 70, in serve
    await self._serve(sockets)
  File "/usr/local/lib/python3.12/site-packages/uvicorn/server.py", line 77, in _serve
    config.load()
  File "/usr/local/lib/python3.12/site-packages/uvicorn/config.py", line 435, in load
    self.loaded_app = import_from_string(self.app)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/uvicorn/importer.py", line 22, in import_from_string
    raise exc from None
  File "/usr/local/lib/python3.12/site-packages/uvicorn/importer.py", line 19, in import_from_string
    module = importlib.import_module(module_str)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/importlib/__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "&lt;frozen importlib._bootstrap&gt;", line 1387, in _gcd_import
  File "&lt;frozen importlib._bootstrap&gt;", line 1360, in _find_and_load
  File "&lt;frozen importlib._bootstrap&gt;", line 1331, in _find_and_load_unlocked
  File "&lt;frozen importlib._bootstrap&gt;", line 935, in _load_unlocked
  File "&lt;frozen importlib._bootstrap_external&gt;", line 999, in exec_module
  File "&lt;frozen importlib._bootstrap&gt;", line 488, in _call_with_frames_removed
  File "/app/app.py", line 23, in &lt;module&gt;
    from tasksB import *
  File "/app/tasksB.py", line 83, in &lt;module&gt;
    from flask import Flask, request, jsonify
ModuleNotFoundError: No module named 'flask'
</code></pre>
- **Reactions**: None
- **Post Number**: 436

