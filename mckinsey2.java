public static int count(int n, int[] infectedHouses) {
        Queue<Integer> q = new LinkedList<>();
        Set<Integer> visited = new HashSet<>();
        for (int house: infectedHouses) {
            q.add(house);
            visited.add(house);
        }
        
        int count = 1;
        while (!q.isEmpty()) {
            int qSize = q.size();
            for (int i = 0; i < q.size(); i++) {
                int house = q.poll();
                if (house - 1 >= 1 && !visited.contains(house - 1)) {
                    visited.add(house - 1);
                    q.add(house - 1);
                }
                
                if (house + 1 <= n && !visited.contains(house + 1)) {
                    visited.add(house + 1);
                    q.add(house + 1);
                }
            }
            
            count *= factorial(q.size());
        }
        
        return count;
    }
    
    private static int factorial(int n) {
        int x = 1;
        while (n > 1) {
            x *= n;
            n -= 1;
        }
        
        return x;
    }