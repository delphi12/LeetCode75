"""1. Code Question 1

The developers at Amazon want to perform a reliability drill on some servers.
There are n servers where the ith server can serve request[i] number of requests and has an
initial health of health[i] units.

Each second, the developers send the maximum possible number of requests that can be served by all the
available servers. With the request, the developers can also send a virus to one of the servers that can
decrease the health of a particular server by k units. The developers can choose the server where the virus
should be sent.
A server goes down when its health is less than or equal to 0.
After all the servers are down, the developers must send one more request to conclude the failure of the
application.
Find the minimum total number of requests that the developers must use to bring all the servers down.
Example
Consider n = 2, request = [3, 4], health = [4, 6], k=
The minimum number of requests required is 21."""

def getMinRequests(request, health, k):

    n= len(request);
    total_requests = 0
    temp = n-1;

    while(temp>=0):
        max_requests = 0
        for i in range(n):
            if health[i] > 0:
                max_requests += request[i]
        total_requests += max_requests

        if(health[temp]>0):
            health[temp]-=k
        elif(temp>=0):
            temp-=1
            health[temp]-=k
        else:
            temp-=1

    total_requests += 1
    return total_requests

"""request = [1,2,3]
health=[3,2,1]
k=2
print(getMinRequests(request,health,k)) #output should be 12"""

request =[3,4]
health =[4,6]
k=3
print(getMinRequests(request, health, k)) #output should be 21