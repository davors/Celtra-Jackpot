%average values from same points
%d: first column must contain score, other columns contain parameter values
%parIdx: array that specifies which parameters to consider when averaging score, values must be >= 1
%dout: is always of size 
function dout = FuncAvgSamePoints(d,parIdx)

parIdx = parIdx + 1;            %correct indexes in d matrix (first column is score)
dout = sortrows(d,parIdx);      %sort by all parameters
dout = dout(:,[1 parIdx]);
same_count = 1;
previous_index = 1;
new_count = 1;
for i = 2:size(dout,1)
    if (sum(dout(i,2:end) == dout(previous_index,2:end)) == size(parIdx,2))   %check if samples are equal
        dout(previous_index,1) = (dout(previous_index,1) * same_count + dout(i,1)) / (same_count+1);
        same_count = same_count +1;
    else
        dout(new_count,:) = dout(previous_index,:);
        new_count = new_count + 1;
        same_count = 1;
        previous_index = i;
    end
end
dout(new_count,:) = dout(previous_index,:);   %last sample
dout = dout(1:new_count,:);

end