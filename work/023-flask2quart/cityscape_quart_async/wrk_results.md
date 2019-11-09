Performance Results for Comparison of Sync vs. Async
====================================================

# Setup

The Flask app is run with hypercorn like so:
```
hypercorn app:app -b 127.0.0.1:5000
```

# Weather Endpoint
```
$ wrk -c20 -t20 -d15s http://localhost:5000/api/weather/96727/us
Running 15s test @ http://localhost:5000/api/weather/96727/us
  20 threads and 20 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     0.00us    0.00us   0.00us     nan%
    Req/Sec     0.00      0.00     0.00    100.00%
  39 requests in 15.11s, 21.75KB read
  Socket errors: connect 0, read 0, write 0, timeout 39
Requests/sec:      2.58
Transfer/sec:      1.44KB
```

# Sun Endpoint
```
$ wrk -c20 -t20 -d15s http://localhost:5000/api/sun/96727/us
Running 15s test @ http://localhost:5000/api/sun/96727/us
  20 threads and 20 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     0.00us    0.00us   0.00us     nan%
    Req/Sec     0.00      0.00     0.00    100.00%
  1 requests in 15.07s, 465.00B read
  Socket errors: connect 0, read 0, write 0, timeout 1
Requests/sec:      0.07
Transfer/sec:      30.85B
```

# Summary

Looks like with both implementation, almost all the requests did timeout. 
I have a very bad connection where I am (especially now), so this is probably not a good setup for a test.
