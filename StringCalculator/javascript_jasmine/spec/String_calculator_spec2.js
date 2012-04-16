describe("String Calculator", function() {
    var sc;
    
    beforeEach(function() {
        sc = new StringCalculator();
    });
    
    describe("#Adding", function() {
        it("should return 0 with empty input", function() {
            val = sc.add("");
            expect(val).toEqual(0);
        });
        
        it("should return the sum of two given values separated by comma", function() {
            val = sc.add("1,2");
            expect(val).toEqual(3);
        });
        
        it("should return the sum of any given values separated by comma", function() {
            val = sc.add("1,2,3,4,5,6,7")
            expect(val).toEqual(28);
        });
        
        it("should accepts newline as a separator instead of comma", function() {
            val = sc.add("1\n2\n3");
            expect(val).toEqual(6);
        });
        
        it("should accept specified delimeter", function() {
            val = sc.add("//#\n1#2#3");
            expect(val).toEqual(6);
        });
        
        it("should throw exception if there is a negative number in input", function() {
            expect(function() {
                val = sc.add("1,-2,3")
            }).toThrow("negatives not allowed -2");
        });
        
        it("should display all the negative numbers when throwing the exception", function() {
            expect(function() {
                val = sc.add("1,-2,-3,-4,5")
            }).toThrow("negatives not allowed -2 -3 -4");
        
        });
        
        it("should ignore numbers that are bigger than 1000", function() {
            val = sc.add("1,1001,2")
            expect(val).toEqual(3);
        });
        
        it("should accept anything as delimiter", function() {
            val = sc.add("//[***]\n1***2***3");
            expect(val).toEqual(6);
        });
        
        it("should allow multiple delimeters", function() {
            val = sc.add("//[*][%]\n1*2%3");
            expect(val).toEqual(6);
        });
        
        it("should allow multiple multiple character delimeters", function() {
            val = sc.add("//[*xb][%%!]\n1*xb2%%!3");
            expect(val).toEqual(6);
        
        });
    });
});