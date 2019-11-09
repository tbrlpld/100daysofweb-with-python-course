Performance Results for Comparison of Sync vs. Async
====================================================

# Setup

The Flask app is run with gunicorn like so:
```
gunicorn app:app -b 127.0.0.1:5000
```

# Weather Endpoint
```
$ wrk -c20 -t20 -d15s http://localhost:5000/api/weather/96727/us
Running 15s test @ http://localhost:5000/api/weather/96727/us
  20 threads and 20 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     1.35s     0.00us   1.35s   100.00%
    Req/Sec     0.00      0.00     0.00    100.00%
  10 requests in 15.06s, 5.81KB read
  Socket errors: connect 0, read 0, write 0, timeout 9
Requests/sec:      0.66
Transfer/sec:     395.03B
```

# Sun Endpoint
```
$ wrk -c20 -t20 -d15s http://localhost:5000/api/sun/96727/us
Running 15s test @ http://localhost:5000/api/sun/96727/us
  20 threads and 20 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     0.00us    0.00us   0.00us     nan%
    Req/Sec     0.00      0.00     0.00    100.00%
  8 requests in 15.05s, 3.82KB read
  Socket errors: connect 0, read 0, write 0, timeout 8
Requests/sec:      0.53
Transfer/sec:     259.93B
```