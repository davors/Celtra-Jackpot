%input format type:     score   p1 p2 p3 ...
%output format type:    percentage_of_all_samples  num_samples  score p1 p2 p3 ...    confScore c1 c2 c3...     m1 m2 m3 ...
%   p - mean parameter value, c - confidence for average value, m - median parameter value
function best_settings = FuncCalcAvgBestSamples(d,percentageBest,calucalte_average_values_step_ratio,use_num_evaluations_for_confidence,assume_binomial_score_distribution,num_evaluations_per_score)

num_rows = size(d,2);
num_samples = size(d,1);

best_settings = zeros(percentageBest+1, 2 + num_rows + num_rows + num_rows-1);

d = sortrows(d,1);


fprintf('\n');
fprintf('Num best \t \t scr \t  cnf \t \t ');
for i = 1:(num_rows-1)
    fprintf(' \t P%d      cnf      median \t ',i);
end
fprintf('\n');

for i = percentageBest+1:-1:1

    num_best_samples = round(max(1 , num_samples*(i-1)/100.0*calucalte_average_values_step_ratio));

    best_settings(i, 1) = (i-1)*calucalte_average_values_step_ratio;
    best_settings(i, 2) = num_best_samples;
    
    %average values    
    best_settings(i, 3:2+num_rows) = mean(d(end-num_best_samples+1:end,1:end),1);
    
    %confidence interval 95%
    if(num_best_samples > 1)    
        best_settings(i, 3+num_rows:3+num_rows+num_rows-1) = std(d(end-num_best_samples+1:end,1:end),0,1) * 1.960 / sqrt(num_best_samples); %confidence 95% (also for score)
    else
        best_settings(i, 3+num_rows:3+num_rows+num_rows-1) = 0;
    end
    
    %medians (not for score, that is why it goes from 2:end instead of 1:end)
    best_settings(i, 3+num_rows+num_rows:end) = median(d(end-num_best_samples+1:end,2:end),1);    
    
    %confidence based on number of evaluations made before matlab
    if(use_num_evaluations_for_confidence)
       if(assume_binomial_score_distribution)
           %binomial equation for confidence: c95 = sqrt(1.96*1.96*avg*(1-avg)/n)
           best_settings(i, 3+num_rows) = sqrt(1.96*1.96*(best_settings(i, 3)/100)*(1-best_settings(i, 3)/100)*2/ (num_best_samples*num_evaluations_per_score)) * 100;
       end
    end
    
    fprintf('%5.2f%% (%2d)', best_settings(i, 1), best_settings(i, 2));
    fprintf(' \t %6.4f  %5.4f \t ', best_settings(i, 2+1), best_settings(i, 2+num_rows+1)); %print score
    for p = 2:num_rows  %print parameter values
        fprintf(' \t %6.4f  %5.4f  %6.4f \t ', best_settings(i, 2+p), best_settings(i, 2+num_rows+p), best_settings(i,2+num_rows+num_rows-1+p));
    end
    fprintf('\n');
end
fprintf('\n');

end