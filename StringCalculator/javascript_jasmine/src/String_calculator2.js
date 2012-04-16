function StringCalculator() {
    this.add = function(values) {
        sum = 0;
        if (values.length > 0) {
            splittedValues = handleDelimeters(values);
            negatives = "";
            _.each(splittedValues, function(value) {
                intValue = parseInt(value);
                if (intValue < 0) {
                    negatives += value + " ";
                }
                else if (intValue < 1000)  {
                    sum += parseInt(value);
                }
            });
            if (negatives.length > 0) {
                negatives = negatives.trim();
                throw("negatives not allowed " + negatives);
            }
        }
        return sum;
    }
    
    var handleDelimeters = function(values) {
        if (values.substring(0,2) == "//") {
            delimeterstring = values.substring(2, values.indexOf("\n"));
            delimeters = delimeterstring.match(new RegExp("\\[[^\\]]+\\]", 'gi'));
            if (delimeters == null) {
                delimeters = [];
                delimeters.push(values.substring(2, values.indexOf("\n")));
            }
            _.each(delimeters, function(delim) {
                delim = delim.substring(1, delim.length-1);
                values = values.substring(values.indexOf("\n") + 1, values.length);    
                var newString = values;
                while (newString.indexOf(delim) != -1) {
                    newString = newString.replace(delim, ",");
                }
                //values = values.replace(new RegExp(delim, 'g'), ",");
                values = newString;
            });
        }
        values = values.replace(/\n/g, ",");
        return values.split(",");
    }
}