
vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
    vector<vector<int>> closest_points;
    auto comp = [](vector<int> point1, vector<int> point2) { 
        return sqrt(pow(point1[0], 2) + pow(point1[1], 2)) > 
                    sqrt(pow(point2[0], 2) + pow(point2[1], 2)); 
    };
    make_heap(points.begin(), points.end(), comp);
    for(int i = 0; i < k; ++i) {
        closest_points.push_back(points[0]);
        pop_heap(points.begin(), points.end(), comp);
        points.pop_back();
    }
    return closest_points;
}
