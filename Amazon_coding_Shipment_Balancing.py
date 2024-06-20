"""Amazon has multiple delivery centers for the distribution of its goods.
In one such center, parcels are arranged in a sequence where the ith parcel has a weight of weight/i].
A shipment is constituted of a contiguous segment of parcels in this arrangement. That is, for 3 parcels arranged
with weights [3, 6, 3], a shipment can be formed of parcels with weights [3], [6], [3], [3, 6], [6, 3] and
[3, 6, 3] but not with weights [3, 31. These shipments are to be loaded for delivery and must be balanced.
A shipment is said to be balanced if the weight of the last parcel of the shipment is not the maximum weight
among all the weights in that shipment. For example, shipment with weights [3, 9, 4, 7] is balanced since the
last weight is 7, while the maximum shipment weight is 9.
However, the shipment [4, 7, 2, 7] is not balanced.
Given the weights of n parcels placed in a sequence, find the maximum number of shipments
that can be formed such that each parcel belongs to exactly one shipment, each shipment consists of
only a contiguous segment of parcels, and each shipment is balanced. If there are no balanced shipments,
return 0.


weight = [1, 2, 3, 2, 6, 31
There are n = 6 parcels to ship. The parcels can be
divided into two shipments: [1, 2, 3, 2] and [6, 3), each of which is balanced.
It can also be shown that this is the maximum number of shipments that can be formed. Thus, the answer is 2.
Parcel Weight:
Maximum
Maximum
Last < Maximum
Shipment 1
Last < Maximum
Shipment 2
Function Description
Complete the function findMaximumBalancedShipments in the editor below.
findMaximumBalancedShipments has the following parameter:
int weight[n]: the weights of the parcels
Returns
int: the maximum possible number of balanced shipments that can be formed
Constraints
• 25 n≤ 105
• 1 ≤ weightli] ≤ 10°
• Input Format For Custom Testing
• Sample Case 0
Sample Input For Custom Testing
STDIN
FUNCTION
5
weight[] size n = 5
weight = [8, 5, 4, 7,
2]
54 M
Sample Output
2
Explanation
Form balanced shipments as [[8, 5 1, [4, 7, 21] or [[8, 5, 4], [7, 21]. In either case, the maximum is 2"""


def findMaximumBalancedShipments(weights):
    n = len(weights)
    max_shipments = 0
    current_max = weights[0]
    segment_start = 0

    for i in range(1, n):
        if weights[i] < current_max:
            max_shipments += 1
            if i + 1 < n:
                segment_start = i + 1
                current_max = weights[segment_start]
        else:
            current_max = max(current_max, weights[i])

    return max_shipments

# Sample Input
weights_1 = [8, 5, 4, 7, 2]
print(findMaximumBalancedShipments(weights_1))  # Output should be 2

weights_2 = [1, 2, 3, 2, 6, 3]
print(findMaximumBalancedShipments(weights_2))  # Output should be 2