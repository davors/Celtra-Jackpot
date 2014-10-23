%%%%--- USE first_data_column = 1 FROM experiment_filenames{1} to {59} !!!! ---%%%%

%list of available measurements (files) - scores were copied in excel file

experiment_filenames{1}   = 'tmp'
experiment_filenames{2}   = '2014_10_17 first test';
experiment_filenames{3}   = '2014_10_17 first test, case5 start 1.0 2.5';
experiment_filenames{4}   = '2014_10_17 first test, case5 start 0.3 1.5';
experiment_filenames{5}   = '2014_10_17 first test, case5 multiple';

%first experiments: EG on celtra cases (!!! INCORRECT EG IMPLEMENTATION - random in for loop !!!)
experiment_filenames{6}   = 'Jackpot_init.pyc_2014_10_18_01_24_05';    %EG cases celtra 1-5 
experiment_filenames{7}   = 'Jackpot_init.pyc_2014_10_18_02_07_38';    %EG cases celtra 1-5 oracle
experiment_filenames{8}   = 'Jackpot_init.pyc_2014_10_18_01_24_08';    %EG cases celtra 6-10 
experiment_filenames{9}   = 'Jackpot_init.pyc_2014_10_18_02_07_40';    %EG cases celtra 6-10 oracle
experiment_filenames{10}   = 'Jackpot_init.pyc_2014_10_18_02_10_38';    %EG cases celtra 1-10
experiment_filenames{11}   = 'Jackpot_init.pyc_2014_10_18_02_11_04';    %EG cases celtra 1-10 oracle
experiment_filenames{12}   = 'Jackpot_init.pyc_2014_10_18_01_24_57';    %complete with own testcase11, was run by mistake   

%no change point experiments: all strategies on Celtra cases (T1 cases 0-4, T2 cases 5-9, T2 cases 0-9), Or - oracle 0/1
experiment_filenames{13}   = 'Reprint___2014_10_18_EG_T1_Or0___2014_10_19_01_50_01';
experiment_filenames{14}   = '';
experiment_filenames{15}   = 'Reprint___2014_10_18_UCB1_T1_Or0___2014_10_19_01_50_10';
experiment_filenames{16}   = 'Reprint___2014_10_18_UCBT_T1_Or0___2014_10_19_01_50_34';
experiment_filenames{17}   = 'Reprint___2014_10_18_EG_T1_Or1___2014_10_19_01_50_04';
experiment_filenames{18}   = '';
experiment_filenames{19}   = 'Reprint___2014_10_18_UCB1_T1_Or1___2014_10_19_01_50_11';
experiment_filenames{20}   = 'Reprint___2014_10_18_UCBT_T1_Or1___2014_10_19_01_50_38';

experiment_filenames{21}   = 'Reprint___2014_10_18_EG_T2_Or0___2014_10_19_01_50_06';
experiment_filenames{22}   = '';
experiment_filenames{23}   = 'Reprint___2014_10_18_UCB1_T2_Or0___2014_10_19_01_50_13';
experiment_filenames{24}   = 'Reprint___2014_10_18_UCBT_T2_Or0___2014_10_19_01_50_41';
experiment_filenames{25}   = 'Reprint___2014_10_18_EG_T2_Or1___2014_10_19_01_50_08';
experiment_filenames{26}   = '';
experiment_filenames{27}   = 'Reprint___2014_10_18_UCB1_T2_Or1___2014_10_19_01_50_15';
experiment_filenames{28}   = 'Reprint___2014_10_18_UCBT_T2_Or1___2014_10_19_01_50_44';

experiment_filenames{29}   = 'Reprint___2014_10_18_EG_T3_Or0___2014_10_18_23_57_07';
experiment_filenames{30}   = 'Reprint___2014_10_18_SMAX_T3_Or0___2014_10_19_00_42_42';
experiment_filenames{31}   = 'Reprint___2014_10_18_UCB1_T3_Or0___2014_10_18_12_35_45';
experiment_filenames{32}   = 'Reprint___2014_10_18_UCBT_T3_Or0___2014_10_18_12_36_16';
experiment_filenames{33}   = 'Reprint___2014_10_18_EG_T3_Or1___2014_10_18_23_57_10';
experiment_filenames{34}   = 'Reprint___2014_10_18_SMAX_T3_Or1___2014_10_18_21_38_03';
experiment_filenames{35}   = 'Reprint___2014_10_18_UCB1_T3_Or1___2014_10_18_12_35_18';
experiment_filenames{36}   = 'Reprint___2014_10_18_UCBT_T3_Or1___2014_10_18_12_37_21';

%2014_10_20 DavorTom change point experiments
experiment_filenames{37}   = 'Reprint___2014_10_20_UCBT_T3_Or1_parTHR_ResetZero___2014_10_20_01_24_54';
experiment_filenames{38}   = 'Reprint___2014_10_20_UCBT_T3_Or1_parTHR_ResetAllMA___2014_10_20_01_24_47';
experiment_filenames{39}   = 'Reprint___2014_10_20_UCBT_T3_Or1_parTHR_ResetCut___2014_10_20_01_24_49';
experiment_filenames{40}   = 'Reprint___2014_10_20_UCBT_T3_Or1_parTHR_ResetSingle___2014_10_20_01_24_52';

experiment_filenames{41}   = 'Reprint___2014_10_20_UCBT_T3_Or0_Shr1.0_Min50_ResetZero___2014_10_20_00_01_05';
experiment_filenames{42}   = 'Reprint___2014_10_20_UCBT_T3_Or0_Shr1.0_Min50_ResetAllMA___2014_10_20_00_01_50';
experiment_filenames{43}   = 'Reprint___2014_10_20_UCBT_T3_Or0_Shr1.0_Min50_ResetCut___2014_10_20_00_02_16';
experiment_filenames{44}   = 'Reprint___2014_10_20_UCBT_T3_Or0_Shr1.0_Min50_ResetSingle___2014_10_20_00_02_45';

experiment_filenames{45}   = 'Reprint___2014_10_20_UCBT_T3_Or0_4par_ResetZero___2014_10_20_01_25_55';
experiment_filenames{46}   = 'Reprint___2014_10_20_UCBT_T3_Or0_4par_ResetAllMA___2014_10_20_01_25_30';
experiment_filenames{47}   = 'Reprint___2014_10_20_UCBT_T3_Or0_4par_ResetCut___2014_10_20_01_25_39';
experiment_filenames{48}   = 'Reprint___2014_10_20_UCBT_T3_Or0_4par_ResetSingle___2014_10_20_01_25_51';

experiment_filenames{49}   = 'Reprint___2014_10_20_UCBT_T3_Or0_Shr0.6_Min50_ResetZero___2014_10_20_09_25_50';
experiment_filenames{50}   = 'Reprint___2014_10_20_UCBT_T3_Or0_Shr0.6_Min50_ResetAllMA___2014_10_20_09_25_42';
experiment_filenames{51}   = 'Reprint___2014_10_20_UCBT_T3_Or0_Shr0.6_Min50_ResetCut___2014_10_20_09_25_44';
experiment_filenames{52}   = 'Reprint___2014_10_20_UCBT_T3_Or0_Shr0.6_Min50_ResetSingle___2014_10_20_09_25_48';

experiment_filenames{53}   = 'Reprint___2014_10_20_UCBT_T3_Or1_2par(CT,CI)_ResetZero___2014_10_20_09_53_05';
experiment_filenames{54}   = 'Reprint___2014_10_20_UCBT_T3_Or1_2par(CT,CI)_ResetAllMA___2014_10_20_09_51_26';
experiment_filenames{55}   = 'Reprint___2014_10_20_UCBT_T3_Or1_2par(CT,CI)_ResetCut___2014_10_20_09_54_49';
experiment_filenames{56}   = 'Reprint___2014_10_20_UCBT_T3_Or1_2par(CT,CI)_ResetSingle___2014_10_20_09_48_44';

experiment_filenames{57}   = '';
experiment_filenames{58}   = '';
experiment_filenames{59}   = '';

%%%%--- USE first_data_column = 2 FROM HERE ON !!!! ---%%%%
%2014_10_21
experiment_filenames{60}   = 'Reprint___2014_10_21_UCBT_4parms_resetSingle___2014_10_21_00_30_42';
experiment_filenames{61}   = 'Reprint___2014_10_21_UCBT_2parms_resetSingle___2014_10_21_01_19_20';
experiment_filenames{62}   = 'Reprint___2014_10_21_Or1_UCBT_3parms_resetSingle___2014_10_20_13_19_04';

experiment_filenames{63}   = 'Reprint___2014_10_21_T3_Or0_Egre_CPthr_resetCut___2014_10_21_01_19_20';
experiment_filenames{64}   = 'Reprint___2014_10_21_T3_Or0_Egre_CPthr_resetMA___2014_10_21_01_19_20';
experiment_filenames{65}   = 'Reprint___2014_10_21_T3_Or0_Egre_CPthr_resetSingle___2014_10_21_01_19_20';
experiment_filenames{66}   = 'Reprint___2014_10_21_T3_Or0_Egre_CPthr_resetZero___2014_10_21_01_19_20';

experiment_filenames{67}   = 'Reprint___2014_10_21_T3_Or0_UCB1_CPthr_resetCut___2014_10_21_01_19_20';
experiment_filenames{68}   = 'Reprint___2014_10_21_T3_Or0_UCB1_CPthr_resetMA___2014_10_21_01_19_20';
experiment_filenames{69}   = 'Reprint___2014_10_21_T3_Or0_UCB1_CPthr_resetSingle___2014_10_21_01_19_21';
experiment_filenames{70}   = 'Reprint___2014_10_21_T3_Or0_UCB1_CPthr_resetZero___2014_10_21_01_19_20';

experiment_filenames{71}   = 'Reprint___2014_10_21_T3_Or0_UCBT_CPthr_resetCut___2014_10_21_01_19_21';
experiment_filenames{72}   = 'Reprint___2014_10_21_T3_Or0_UCBT_CPthr_resetMA___2014_10_21_01_19_21';
experiment_filenames{73}   = 'Reprint___2014_10_21_T3_Or0_UCBT_CPthr_resetSingle___2014_10_21_01_19_21';
experiment_filenames{74}   = 'Reprint___2014_10_21_T3_Or0_UCBT_CPthr_resetZero___2014_10_21_10_32_18';

%2014_10_21 no change point (redone with improved output)
experiment_filenames{75}   = 'Reprint___2014_10_21_noCPD_Egreedy_perStep10___2014_10_21_19_02_42';
experiment_filenames{76}   = 'Reprint___2014_10_21_noCPD_UCB1_perStep10___2014_10_21_19_04_47';
experiment_filenames{77}   = 'Reprint___2014_10_21_noCPD_UCBT_perStep10___2014_10_21_19_05_39';

%2014_10_21 experiments with more than 10 evaluations per sample
experiment_filenames{78}   = 'Reprint___2014_10_21_noCPD_Egreedy_perStep25___2014_10_21_19_03_05';
experiment_filenames{79}   = 'Reprint___2014_10_21_noCPD_UCB1_perStep25___2014_10_21_19_04_21';
experiment_filenames{80}   = 'Reprint___2014_10_21_noCPD_UCBT_perStep25___2014_10_21_19_06_24';
experiment_filenames{81}   = 'Reprint___2014_10_21_noCPD_UCBT_perStep50___2014_10_21_22_15_21';
experiment_filenames{82}   = 'Reprint___2014_10_21_noCPD_UCBT_perStep100___2014_10_21_22_15_25';

experiment_filenames{90}   = '';
experiment_filenames{91}   = '';

%-------------------- SETTINGS --------------------%
%file read settings

filename_to_load = 83;

analyze_score_for_testCase = 0;
    % 0 ... take average of all
    % > 0 ... analyze for selected testCase

num_header_lines = 17;  %old txt data files had 21
data_delimiter = ' ';
if filename_to_load < 60
    first_data_column = 1;  %if filename_to_load < 60 then it must be 1; otherwise 2
else 
    first_data_column = 2;
end

position_num_final_evaluations = [7 3];    %row and column in file
%position_num_samples = [1 2];               %for safety check
position_num_params = [8 3];                %for safety check

%matlab analysis settings

override_final_evaluations = 0;    %if value is 0 then it is read from the header of the results file, otherwise the value given here is used
use_num_evaluations_for_confidence = true;  %use the number of evaluations (outside of matlab) to calculate score confidence instead of averaging in matlab
assume_binomial_score_distribution = false;  %by default is TRUE for games (win, lose, draw) ... FALSE not yet implemented!

when_identifying_most_reliable_IGNORE_FIRST_N_SAMPLES = 1;   %the number of samples to ignore when identifying max(value - confidence)
                                                             %default = 0
                                                             %useful when assume_binomial_score_distribution = false

calucalte_average_values_to_percent = 40;   %calculate best scores from how many "calucalte_average_values_step_ratio steps" in % of best samples (calculates them all, from the single best down to the given percentage)
calucalte_average_values_step_ratio = 1;    %the step ratio in % to calucalte_average_values_to_percent (this represents the step size in % of number of samples per calculation)
histogram_ignore_outliers_percentage = 1;    %percentage of outliers to ignore (from 0 to 100)
histogram_resolution = 50;      %number of bins in parameter value histogram
histogram_score_step = 0.25;     %score histogram step (resolution in % from 0 to 100)

%display settings
do_not_display_correlation_plots = 1;
do_not_display_3d_plots = 1;
values_decimal_precision = 3;   %default = 2, possible values 1-3

%%------------- END of config section  -------------%%

%TODO naredi da pri corelaciji se zanemari 10% (poljubno nastavljivo) najslabše ocenjenih vzorcev (outliers)

%import data from file
filename = [experiment_filenames{filename_to_load} '.txt'];
importedFile = importdata(filename,data_delimiter,num_header_lines);

tmpstr = strsplit(importedFile.textdata{position_num_params(1)},' ');
input_num_pars = str2double(tmpstr{position_num_params(2)});

d = importedFile.data(:,first_data_column:first_data_column+input_num_pars);

if(analyze_score_for_testCase > 0)
    d(:,1) = importedFile.data(:,first_data_column+input_num_pars+analyze_score_for_testCase);
end

total_num_samples = size(d,1);
num_rows_d = size(d,2);
num_pars_d = num_rows_d - 1;

%check file integrity

% tmpstr = strsplit(importedFile.textdata{position_num_samples(1)},' ');
% if(str2double(tmpstr{position_num_samples(2)}) ~= total_num_samples)
%     warning(['File header mismatch: "' filename '": number of samples does not match!']);
% end

if(input_num_pars ~= num_pars_d)
    warning(['File header mismatch: "' filename '": number of parameters does not match!']);
end
    
%set analysis variables
if(override_final_evaluations > 0)
	num_evaluations_per_score = override_final_evaluations;
else
    tmpstr = strsplit(importedFile.textdata{position_num_final_evaluations(1)},' ');
    num_evaluations_per_score = str2double(tmpstr(position_num_final_evaluations(2)));
end
calucalte_average_values_to_percent = min(calucalte_average_values_to_percent, total_num_samples);
calucalte_average_values_step_ratio = max(calucalte_average_values_step_ratio / (total_num_samples / 100), 100/total_num_samples);
histogram_ignore_outliers_percentage = histogram_ignore_outliers_percentage / 100;

%set display parameters
set(0,'DefaultFigureWindowStyle','docked'); %create plots as tabs in single window
graph_title = experiment_filenames{filename_to_load};

%prepare figures
num_plots_single = num_pars_d * 3;
num_plots_general = 5;
num_plots_pairs = num_pars_d*(num_pars_d-1)/2;

num_figs_single = floor((num_pars_d+2)/3);
num_figs_general = floor((num_plots_general+5)/6);
num_figs_pairs = floor((num_plots_pairs-1+5)/6);
if(num_plots_pairs > 7)
    num_figs_pairs = num_figs_pairs + 1;
end

%preallocate array of figure handlers
all_figs(num_figs_single+num_figs_general+num_figs_pairs) = figure(1);
all_plots(num_plots_single+num_plots_general+num_plots_pairs+num_plots_pairs) = subplot(3,3,1);
num_figures = 0;
num_plots = 0;

%prepare color map
cmap = lines(num_pars_d+1);

%create parameters legend
pars_legend_string = cell(num_pars_d,1);
for i = 1 : num_pars_d
    pars_legend_string{i} = ['p' num2str(i-1)];
end


%%------------- BEGIN ANALYSIS -------------%%

%calculate scores of selected percentage of best scored samples
best_settings = FuncCalcAvgBestSamples(d,calucalte_average_values_to_percent,calucalte_average_values_step_ratio,use_num_evaluations_for_confidence,assume_binomial_score_distribution,num_evaluations_per_score);

%find most reliable setting (max(score-confidence95))
[most_reliable_setting_min_score , most_reliable_setting_index] = max(best_settings(when_identifying_most_reliable_IGNORE_FIRST_N_SAMPLES+2:end,3)-best_settings(when_identifying_most_reliable_IGNORE_FIRST_N_SAMPLES+2:end,3+num_pars_d+1));
most_reliable_setting_index = most_reliable_setting_index + when_identifying_most_reliable_IGNORE_FIRST_N_SAMPLES + 1;
most_reliable_setting_avg_score = best_settings(most_reliable_setting_index,3);
most_reliable_setting_num_samples = best_settings(most_reliable_setting_index,2);

% --- plot relations between individual parameters and score --- %
for i = 1:num_pars_d
    
    %create next figure every 
    if( mod(i,3) == 1 )
        num_figures = num_figures + 1;
        all_figs(num_figures) = figure(num_figures);
        clf(all_figs(num_figures));
        % Enlarge figure to full screen.
        %set(fig, 'outerposition',[100 100 1200 800]);
        if(~strcmp(get(0,'DefaultFigureWindowStyle'),'docked'))
            set(all_figs(num_figures), 'units', 'normalized', 'outerposition',[0.05 0.05 0.9 0.9]);
        end
        set(all_figs(num_figures), 'name',['P' num2str(i-1) '-' num2str(min(i+1,num_pars_d-1))],'numbertitle','off') 
        % Give a name to the title bar.
    end
    
    %plot score by individual parameter
    num_plots = num_plots + 1;
    all_plots(num_plots) = subplot(3,3,mod(i-1,3)*3 + 1);
    hold off
    [sort_par, sort_par_ind] = sort(d(:,1+i));
    sort_score = d(sort_par_ind,1);
    plot(sort_par,sort_score,'-','Color',cmap(i+1,:))
    xl = get(gca,'xlim');
    hold on
    plot([0 0], get(gca,'ylim'), '--','color', [0.7 0.7 0.7])       %grey dashed vertical line at 0
    set(gca,'xlim',xl);
    ylabel(pars_legend_string(i));
    if(mod(i-1,3) == 0)
        title('Score by parameter value');
    end
    
    %plot mean (and conf95) and median parameter values for best scores
    num_plots = num_plots + 1;
    all_plots(num_plots) = subplot(3,3,mod(i-1,3)*3 + 2);
    hold off
    plot(best_settings(:,3),best_settings(:,4+num_pars_d+num_pars_d+i),':','Color',cmap(i+1,:));        %median
    hold on
    errorbar(best_settings(:,3),best_settings(:,3+i),best_settings(:,4+num_pars_d+i),'- .','MarkerSize',15,'Color',cmap(i+1,:));    %mean + conf95
    xlim_space = (best_settings(1,3) - best_settings(end,3)) / 20;
    tmp_xlim = [best_settings(end,3)-xlim_space best_settings(1,3)+xlim_space];
    if tmp_xlim(2) == tmp_xlim(1)
       tttv = tmp_xlim(1)*0.01;
       tmp_xlim(2) = tmp_xlim(2)+tttv;
       tmp_xlim(1) = tmp_xlim(1)-tttv;
    end
    yl = get(gca,'ylim');
    plot(tmp_xlim, [0 0],'--','color', [0.7 0.7 0.7])       %grey dashed horizontal line at 0
    set(gca,'ylim',yl);
    xlim(tmp_xlim);
    plot([most_reliable_setting_avg_score most_reliable_setting_avg_score],get(gca,'ylim'),'-','color', [0.7 0.7 0.7])     %vertical line at most reliable setting (max(avg-conf95))
    set(gca,'children',flipud(get(gca,'children'))) %bring to front in reverse order as plotted
    %if(mod(i-1,3) == 0)
        title('Averaged parameter value by best scores');
        if(values_decimal_precision == 1)
            legend_text1 = sprintf('%4.1f \tMedian\n%4.1f \tMean\n%4.1f \tConfidence int. 95%%', best_settings(most_reliable_setting_index,4+num_pars_d+num_pars_d+i), best_settings(most_reliable_setting_index,3+i), best_settings(most_reliable_setting_index,4+num_pars_d+i));
        elseif(values_decimal_precision == 3)
            legend_text1 = sprintf('%6.3f \tMedian\n%6.3f \tMean\n%6.3f \tConfidence int. 95%%', best_settings(most_reliable_setting_index,4+num_pars_d+num_pars_d+i), best_settings(most_reliable_setting_index,3+i), best_settings(most_reliable_setting_index,4+num_pars_d+i));
        else
            legend_text1 = sprintf('%5.2f \tMedian\n%5.2f \tMean\n%5.2f \tConfidence int. 95%%', best_settings(most_reliable_setting_index,4+num_pars_d+num_pars_d+i), best_settings(most_reliable_setting_index,3+i), best_settings(most_reliable_setting_index,4+num_pars_d+i));
        end
        h_legend = legend(legend_text1,'Location','Best','Orientation','horizontal');    
        set(h_legend,'Fontname','Bitstream Vera Sans Mono');
    %end

    %plot histogram of values found by LRP
    num_plots = num_plots + 1;
    all_plots(num_plots) = subplot(3,3,mod(i-1,3)*3 + 3);
    hold off
    hist_lower = sort_par(max(1,floor(length(sort_par)*histogram_ignore_outliers_percentage)));
    hist_upper = sort_par(min(length(sort_par),floor(length(sort_par)*(1-histogram_ignore_outliers_percentage))));
    histogram_parameter_range = linspace(hist_lower,hist_upper,histogram_resolution);
    hist(sort_par,histogram_parameter_range,'Color',cmap(i+1,:));
    %[hist_f,hist_x] = hist(sort_par,histogram_parameter_range);
    %bar(hist_x,hist_f/trapz(hist_x,hist_f),1);
    h = findobj(gca,'Type','patch');
    set(h,'FaceColor',cmap(i+1,:),'EdgeColor',cmap(i+1,:));
    if(min(histogram_parameter_range) < max(histogram_parameter_range))
        xlim([min(histogram_parameter_range) max(histogram_parameter_range)]);
    end
    hold on
    if(mod(size(sort_par,1),2) == 0)
        par_median = (sort_par(floor(size(sort_par,1)*0.5)) + sort_par(floor(size(sort_par,1)*0.5)+1)) / 2;
    else
        par_median = sort_par(floor(size(sort_par,1)*0.5));
    end
    h1 = plot([par_median par_median],get(gca,'ylim'),':','color', [0 0 0],'LineWidth',2);    %vertical line at median
    par_mean = mean(sort_par);
    h2 = plot([par_mean par_mean],get(gca,'ylim'),'-','color', [0 0 0],'LineWidth',2);    %vertical line at median
    %if(mod(i-1,3) == 0)
        title('Parameter value histogram');
        if(values_decimal_precision == 1)
            h_legend = legend([h1 h2],{sprintf('Median\t %4.1f',par_median); sprintf('Mean  \t %4.1f',par_mean)},'Location','Best','Orientation','vertical');
        elseif(values_decimal_precision == 3)
            h_legend = legend([h1 h2],{sprintf('Median\t %6.3f',par_median); sprintf('Mean  \t %6.3f',par_mean)},'Location','Best','Orientation','vertical');
        else
            h_legend = legend([h1 h2],{sprintf('Median\t %5.2f',par_median); sprintf('Mean  \t %5.2f',par_mean)},'Location','Best','Orientation','vertical');
        end
        set(h_legend,'Fontname','Bitstream Vera Sans Mono');
    %end    
end

% --- END - plot relations between individual parameters and score --- %

% --- plot general summary --- %

%prepare figure
num_figures = num_figures + 1;
summary_figure = num_figures;
all_figs(num_figures) = figure(num_figures);
clf(all_figs(num_figures));
if(~strcmp(get(0,'DefaultFigureWindowStyle'),'docked'))
    set(all_figs(num_figures), 'units', 'normalized', 'outerposition',[0.05 0.05 0.9 0.9]);
end
set(all_figs(num_figures), 'name','Summary','numbertitle','off')

%plot all params avg only
num_plots = num_plots + 1;
all_plots(num_plots) = subplot(2,3,2);

hold off
i = 1;
plot(best_settings(:,3),best_settings(:,3+i),'- .','MarkerSize',15,'Color',cmap(i+1,:));
%errorbar(best_settings(:,3),best_settings(:,3+i),best_settings(:,4+num_pars_d+i),'- .','MarkerSize',15,'Color',cmap(i+1,:));  %with confidence errorbars
hold on
for i = 2:num_pars_d
    plot(best_settings(:,3),best_settings(:,3+i),'- .','MarkerSize',15,'Color',cmap(i+1,:));
    %errorbar(best_settings(:,3),best_settings(:,3+i),best_settings(:,4+num_pars_d+i),'- .','MarkerSize',15,'Color',cmap(i+1,:));  %with confidence errorbars
end
tmp_xlim = [best_settings(end,3)-xlim_space best_settings(1,3)+xlim_space];
if tmp_xlim(2) == tmp_xlim(1)
   tttv = tmp_xlim(1)*0.01;
   tmp_xlim(2) = tmp_xlim(2)+tttv;
   tmp_xlim(1) = tmp_xlim(1)-tttv;
end
plot(tmp_xlim, [0 0],'--','color', [0.7 0.7 0.7])       %grey horizontal line at 0
xlim(tmp_xlim);
plot([most_reliable_setting_avg_score most_reliable_setting_avg_score],get(gca,'ylim'),'-','color', [0.7 0.7 0.7])     %vertical line at most reliable setting (max(avg-conf95))
legend_text = pars_legend_string;
for i = 1:num_pars_d
    if(values_decimal_precision == 1)
        legend_text{i} = sprintf('%s\n% 3.1f\n%c%3.1f',legend_text{i},best_settings(most_reliable_setting_index,3+i),177,best_settings(most_reliable_setting_index,4+num_pars_d+i));
    elseif(values_decimal_precision == 3)
        legend_text{i} = sprintf('%s\n% 5.3f\n%c%5.3f',legend_text{i},best_settings(most_reliable_setting_index,3+i),177,best_settings(most_reliable_setting_index,4+num_pars_d+i));
    else
        legend_text{i} = sprintf('%s\n% 4.2f\n%c%4.2f',legend_text{i},best_settings(most_reliable_setting_index,3+i),177,best_settings(most_reliable_setting_index,4+num_pars_d+i));
    end
end
if(num_pars_d > 2)
    h_legend = legend(legend_text,'Location','NorthOutside','Orientation','horizontal');
else
    h_legend = legend(legend_text,'Location','Best','Orientation','vertical');    
end
set(h_legend,'Fontname','Bitstream Vera Sans Mono');
set(gca,'children',flipud(get(gca,'children'))) %bring to front in reverse order as plotted, disrupts the legend if called before it
%ylim_max = max(max(best_settings(most_reliable_setting_index,4:3+num_pars_d)));
%ylim_min = min(min(best_settings(most_reliable_setting_index,4:3+num_pars_d)));
ylim_max = max(max(best_settings(:,4:3+num_pars_d)));
ylim_min = min(min(best_settings(:,4:3+num_pars_d)));
ylim_space = (ylim_max - ylim_min) / 20;
ylim([(ylim_min-ylim_space) (ylim_max+ylim_space)]);
title('Average parameter value');
xlabel('Best score');

%plot all params abs(avg-conf)
num_plots = num_plots + 1;
all_plots(num_plots) = subplot(2,3,5);
                
hold off
i = 1;
plot(best_settings(:,3),abs(best_settings(:,3+i))-best_settings(:,4+num_pars_d+i),'- .','MarkerSize',15,'Color',cmap(i+1,:));
hold on
for i = 2:num_pars_d
    plot(best_settings(:,3),abs(best_settings(:,3+i))-best_settings(:,4+num_pars_d+i),'- .','MarkerSize',15,'Color',cmap(i+1,:));
end
tmp_xlim = [best_settings(end,3)-xlim_space best_settings(1,3)+xlim_space];
if tmp_xlim(2) == tmp_xlim(1)
   tttv = tmp_xlim(1)*0.01;
   tmp_xlim(2) = tmp_xlim(2)+tttv;
   tmp_xlim(1) = tmp_xlim(1)-tttv;
end
plot(tmp_xlim, [0 0],'--','color', [0.7 0.7 0.7])       %grey horizontal line at 0
xlim(tmp_xlim);
plot([most_reliable_setting_avg_score most_reliable_setting_avg_score],get(gca,'ylim'),'-','color', [0.7 0.7 0.7])     %vertical line at most reliable setting (max(avg-conf95))
legend_text = pars_legend_string;
for i = 1:num_pars_d
    if(values_decimal_precision == 1)
        legend_text{i} = sprintf('%s\n%+3.1f',legend_text{i},abs(best_settings(most_reliable_setting_index,3+i))-best_settings(most_reliable_setting_index,4+num_pars_d+i));
    elseif(values_decimal_precision == 3)
        legend_text{i} = sprintf('%s\n%+5.3f',legend_text{i},abs(best_settings(most_reliable_setting_index,3+i))-best_settings(most_reliable_setting_index,4+num_pars_d+i));
    else
        legend_text{i} = sprintf('%s\n%+4.2f',legend_text{i},abs(best_settings(most_reliable_setting_index,3+i))-best_settings(most_reliable_setting_index,4+num_pars_d+i));
    end
end
if(num_pars_d > 2)
    h_legend = legend(legend_text,'Location','NorthOutside','Orientation','horizontal');
else
    h_legend = legend(legend_text,'Location','Best','Orientation','vertical');    
end
set(h_legend,'Fontname','Bitstream Vera Sans Mono');
set(gca,'children',flipud(get(gca,'children'))) %bring to front in reverse order as plotted, disrupts the legend if called before it
%ylim_max = max(max(abs(best_settings(most_reliable_setting_index,4:3+num_pars_d))-best_settings(most_reliable_setting_index,5+num_pars_d:4+num_pars_d+num_pars_d)));
%ylim_min = min(min(abs(best_settings(most_reliable_setting_index,4:3+num_pars_d))-best_settings(most_reliable_setting_index,5+num_pars_d:4+num_pars_d+num_pars_d)));
ylim_max = max(max(abs(best_settings(:,4:3+num_pars_d))-best_settings(:,5+num_pars_d:4+num_pars_d+num_pars_d)));
ylim_min = min(min(abs(best_settings(:,4:3+num_pars_d))-best_settings(:,5+num_pars_d:4+num_pars_d+num_pars_d)));
ylim_space = (ylim_max - ylim_min) / 20;
ylim([max(max(-1,-abs(ylim_max)),ylim_min) (ylim_max+ylim_space)]);
xlabel('Best score');
title('Parameter influence (absolute value minus 95% confidence interval)');

%plot avg scores with confidence 95% by different number of best samples (in %)
num_plots = num_plots + 1;
all_plots(num_plots) = subplot(2,3,1);

hold off;
errorbar(best_settings(:,2),best_settings(:,3),best_settings(:,3+num_pars_d+1),'- .','MarkerSize',15);    
hold on;
%plot([most_reliable_setting_index-1 most_reliable_setting_index-1],get(gca,'ylim'),'color', [0.7 0.7 0.7])    %vertical line at most reliable setting (max(avg-conf95))
plot([most_reliable_setting_num_samples most_reliable_setting_num_samples],get(gca,'ylim'),'color', [0.7 0.7 0.7])    %vertical line at most reliable setting (max(avg-conf95))
set(gca,'children',flipud(get(gca,'children'))) %bring to front in reverse order as plotted
xlim_space = (best_settings(end,2) - best_settings(1,2)) / 20;
xlim([best_settings(1,2)-xlim_space best_settings(end,2)+xlim_space]);
%TODO substitute x-marks with % values
title('Averaged score by number of best samples');
%char(9) -> tab
%char(10) -> new_line
%char(177) -> ±
if(values_decimal_precision == 1)
    legend_text1 = sprintf('Best value minus confidence\n\n%4.1f \tMean (%2d samples)\n%4.1f \tConfidence int. 95%%\n\n%4.1f – %4.1f', most_reliable_setting_avg_score, best_settings(most_reliable_setting_index,2), best_settings(most_reliable_setting_index,3+num_pars_d+1), most_reliable_setting_avg_score-best_settings(most_reliable_setting_index,3+num_pars_d+1),most_reliable_setting_avg_score+best_settings(most_reliable_setting_index,3+num_pars_d+1));
elseif(values_decimal_precision == 3)
    legend_text1 = sprintf('Best value minus confidence\n\n%6.3f \tMean (%2d samples)\n%6.3f \tConfidence int. 95%%\n\n%6.3f – %6.3f', most_reliable_setting_avg_score, best_settings(most_reliable_setting_index,2), best_settings(most_reliable_setting_index,3+num_pars_d+1), most_reliable_setting_avg_score-best_settings(most_reliable_setting_index,3+num_pars_d+1),most_reliable_setting_avg_score+best_settings(most_reliable_setting_index,3+num_pars_d+1));
else
    legend_text1 = sprintf('Best value minus confidence\n\n%5.2f \tMean (%2d samples)\n%5.2f \tConfidence int. 95%%\n\n%5.2f – %5.2f', most_reliable_setting_avg_score, best_settings(most_reliable_setting_index,2), best_settings(most_reliable_setting_index,3+num_pars_d+1), most_reliable_setting_avg_score-best_settings(most_reliable_setting_index,3+num_pars_d+1),most_reliable_setting_avg_score+best_settings(most_reliable_setting_index,3+num_pars_d+1));
end
h_legend = legend(legend_text1,'Location','Best','Orientation','horizontal');
set(h_legend,'Fontname','Bitstream Vera Sans Mono');


%plot score histogram
[sort_scr, sort_scr_ind] = sort(d(:,1));
hist_lower = sort_scr(max(1,floor(length(sort_scr)*histogram_ignore_outliers_percentage)));
hist_upper = sort_scr(min(length(sort_par),floor(length(sort_scr)*(1-histogram_ignore_outliers_percentage))));
score_hist_bins = max(hist_lower-5,0):histogram_score_step:min(hist_upper+5,100);
num_plots = num_plots + 1;
all_plots(num_plots) = subplot(2,3,4);

hold off;
hist(d(:,1),score_hist_bins);
%[hist_f,hist_x]=hist(d(:,1),score_hist_bins);
%bar(hist_x,hist_f/trapz(hist_x,hist_f),1);     %TODO histogram with BAR, with relative zone calc ... also for parameters, commented out because for params it was not working ok because of the changed xlim
h = findobj(gca,'Type','patch');
set(h,'FaceColor','blue','EdgeColor','blue');
hold on
if(mod(size(sort_scr,1),2) == 0)
    par_median = (sort_scr(floor(size(sort_scr,1)*0.5)) + sort_scr(floor(size(sort_scr,1)*0.5)+1)) / 2;
else
    par_median = sort_scr(floor(size(sort_scr,1)*0.5));
end
score_median = median(d(:,1));
h1 = plot([score_median score_median],get(gca,'ylim'),':','color', [0 0 0],'LineWidth',2);    %vertical line at median
score_mean = mean(d(:,1));
h2 = plot([score_mean score_mean],get(gca,'ylim'),'-','color', [0 0 0],'LineWidth',2);    %vertical line at median
xlim([max(0,min(score_hist_bins)-histogram_score_step) min(100,max(score_hist_bins)+histogram_score_step)]);
title('Score histogram');
if(values_decimal_precision == 1)
    h_legend = legend([h1 h2],{sprintf('Median\t %4.1f',score_median); sprintf('Mean  \t %4.1f',score_mean)},'Location','Best','Orientation','vertical');
elseif(values_decimal_precision == 3)
    h_legend = legend([h1 h2],{sprintf('Median\t %6.3f',score_median); sprintf('Mean  \t %6.3f',score_mean)},'Location','Best','Orientation','vertical');
else
    h_legend = legend([h1 h2],{sprintf('Median\t %5.2f',score_median); sprintf('Mean  \t %5.2f',score_mean)},'Location','Best','Orientation','vertical');
end
set(h_legend,'Fontname','Bitstream Vera Sans Mono');

%bar(X, N./sum(N), 1);
%title('score','FontSize',12);
%xlim([0 100]);


% --- END - plot general summary --- %


% --- calculate correlations --- %

if(do_not_display_correlation_plots)
    
    correlations = corrcoef(d);
    
else

    %prepare figure
    num_figures = num_figures + 1;
    all_figs(num_figures) = figure(num_figures);
    if(~strcmp(get(0,'DefaultFigureWindowStyle'),'docked'))
        set(all_figs(num_figures), 'units', 'normalized', 'outerposition',[0.05 0.05 0.9 0.9]);
    end
    set(all_figs(num_figures), 'name','Correlations','numbertitle','off')

    %create correlations plot
    correlations = corrplot(d,'varNames',['score'; pars_legend_string]);       %default: Pearson

    % corrplot(d(:,2:end),'varNames',pars_legend_string);         %default: Pearson
    % corrplot(d(:,2:end),'varNames',pars_legend_string,'type','Kendall');
    % corrplot(d(:,2:end),'varNames',pars_legend_string,'type','Spearman');

    %copy corrplot to appropriate figure and delete the figure created by corrplot()
    all_figures = get(0,'Children');
    tmpFig = all_figures(1);         %last created figure is first in array
    hold off
    if(tmpFig ~= num_figures)    
        clf(all_figs(num_figures));
        copyobj(get(tmpFig,'children'), all_figs(num_figures));
        close(tmpFig);
    end
    
end


%plot correlation matrix on the summary figure
figure(summary_figure);
num_plots = num_plots + 1;
all_plots(num_plots) = subplot(2,3,3);

unfreezeColors

cvis = correlations - diag(diag(correlations));
imagesc(cvis);
cmap = load('colormap_blue_white_red.m');
colormap(cmap)
colorbar('location','EastOutside')
caxis([-1.0, +1.0]);

ax1 = gca;
set(ax1, 'XTick', 1:size(cvis,1), 'YTick', 1:size(cvis,2));
set(ax1, 'XTickLabel',['score';pars_legend_string],'YTickLabel',['score';pars_legend_string])

if(values_decimal_precision == 1)
    textStrings = strtrim(cellstr(num2str(cvis(:),'%0.1f')));  %# Create strings from the matrix values
elseif(values_decimal_precision == 3)
    textStrings = strtrim(cellstr(num2str(cvis(:),'%0.3f')));  %# Create strings from the matrix values
else
    textStrings = strtrim(cellstr(num2str(cvis(:),'%0.2f')));  %# Create strings from the matrix values
end

[tx,ty] = meshgrid(1:size(cvis,1));                 %# Create x and y coordinates for the strings
hStrings = text(tx(:),ty(:),textStrings(:),'HorizontalAlignment','center');      %# Plot the strings
textColors = repmat(((cvis(:) > 0.55)+(cvis(:) < -0.55)),1,3);  %# Choose white or black for the text color of the strings so they can be easily seen over the background color
set(hStrings,{'Color'},num2cell(textColors,2));             %# Change the text colors

title({'Correlation coeficients';' '});

freezeColors
cbfreeze(colorbar)

ax2 = axes('Position', get(ax1, 'Position'),'Color', 'none');
set(ax2, 'XAxisLocation', 'top','YAxisLocation','Right');
set(ax2, 'XLim', get(ax1, 'XLim'),'YLim', get(ax1, 'YLim'));
set(ax2, 'XTick', get(ax1, 'XTick'), 'YTick', get(ax1, 'YTick'));
set(ax2, 'XTickLabel', get(ax1,'XTickLabel'),'YTickLabel',[]);
% if not in a SUBPLOT, but as a single plot figure, you need also the following 3 lines of code
% set(ax2, 'Position', get(ax1, 'Position'), 'ActivePositionProperty', get(ax1, 'ActivePositionProperty'), 'Units', get(ax1,'Units'), 'OuterPosition', get(ax1,'OuterPosition'));
% colorbar('location','EastOutside')
% caxis([-1.0, +1.0]);

cbfreeze('off')
unfreezeColors

% --- END - plot all correlations --- %

% --- plot 3d graphs for pairs of parameters --- %

title_once = 1;

%only one subplot
if(num_pars_d == 2)
    
    ip1 = 1;
    ip2 = 2;
    
    da = FuncAvgSamePoints(d,[ip1 ip2]);
    za = da(:,1);
    xa = da(:,2);
    ya = da(:,3);
    
    num_plots = num_plots + 1;
    all_plots(num_plots) = subplot(2,3,6);
    if(total_num_samples > 2)
        FuncDrawSurface(xa,ya,za,'',pars_legend_string(ip1),pars_legend_string(ip2));
        %FuncDrawContour(xa,ya,za,'',pars_legend_string(ip1),pars_legend_string(ip2));
        %FuncDrawColoredPoints(xa,ya,za,0,0,0,'',pars_legend_string(ip1),pars_legend_string(ip2));    
        colormap('jet');

        title('Score by two parameters');
    end
%many subplots over multiple figures
elseif ((num_pars_d > 2)&&(do_not_display_3d_plots == 0))

    %prepare figures
    pairs_current_fig = num_figures;
    for i = 1:max(1,num_figs_pairs-1)
        num_figures = num_figures + 1;
        all_figs(num_figures) = figure(num_figures);
        clf(all_figs(num_figures));
        if(~strcmp(get(0,'DefaultFigureWindowStyle'),'docked'))
            set(all_figs(num_figures), 'units', 'normalized', 'outerposition',[0.05 0.05 0.9 0.9]);
        end
        set(all_figs(num_figures), 'name',['3D_' num2str((i-1)*6) '-' num2str(min((i-1)*6+5,num_plots_pairs-1))],'numbertitle','off')
    end
    if(num_plots_pairs > 7)
        num_figures = num_figures + 1;
        all_figs(num_figures) = figure(num_figures);
        clf(all_figs(num_figures));
        if(~strcmp(get(0,'DefaultFigureWindowStyle'),'docked'))
            set(all_figs(num_figures), 'units', 'normalized', 'outerposition',[0.05 0.05 0.9 0.9]);
        end
        set(all_figs(num_figures), 'name','3D_all','numbertitle','off')
    end

    %plot scores for pairs of parameters
    pairs_current_subplot = 6;
    for ip1 = 1:(num_pars_d-1)
        for ip2 = (ip1+1):num_pars_d

            %increase subplot and figure counters
            pairs_current_subplot = pairs_current_subplot + 1;
            if(pairs_current_subplot >= 7)
                pairs_current_subplot = 1;
                pairs_current_fig = pairs_current_fig + 1;
                figure(pairs_current_fig);
            end
            
            %average values of same points
            da = FuncAvgSamePoints(d,[ip1 ip2]);
            za = da(:,1);
            xa = da(:,2);
            ya = da(:,3);

            num_plots = num_plots + 1;
            all_plots(num_plots) = subplot(2,3,pairs_current_subplot);
            FuncDrawSurface(xa,ya,za,'',pars_legend_string(ip1),pars_legend_string(ip2));
            %FuncDrawContour(xa,ya,za,'',pars_legend_string(ip1),pars_legend_string(ip2));
            %FuncDrawColoredPoints(xa,ya,za,0,0,0,'',pars_legend_string(ip1),pars_legend_string(ip2));        

            if(pairs_current_subplot == 1)
                title('Score by two parameters');
            end
            
            %plot all scores for pairs on single figure
            if(num_plots_pairs > 7)
                set(0,'currentFigure',all_figs(num_figures));   %quiet figure switch
                all_plots(num_plots+num_plots_pairs) = subplot(num_pars_d-1, num_pars_d-1, (ip2-2)*(num_pars_d-1) + ip1);
                FuncDrawSurface(xa,ya,za,'',pars_legend_string(ip1),pars_legend_string(ip2));
                %FuncDrawContour(xa,ya,za,'',pars_legend_string(ip1),pars_legend_string(ip2));
                %FuncDrawColoredPoints(xa,ya,za,0,0,0,'',pars_legend_string(ip1),pars_legend_string(ip2));  
                if((pairs_current_subplot == 1)&&(title_once == 1))
                    title(all_plots(num_plots+num_plots_pairs),'Score by all pairs of parameters');
                    title_once = 0;
                end
                set(0,'currentFigure',all_figs(pairs_current_fig));   %quiet figure switch
            end

        end
    end
    if(num_plots_pairs > 7)
        figure(all_figs(num_figures));
    end
    
end

% --- END - plot 3d graphs for pairs of parameters --- %

figure(summary_figure);

%print best samples
d = d(sort_scr_ind,:);
disp('Best samples:');
disp(d(end-min(most_reliable_setting_num_samples+min(2,total_num_samples-most_reliable_setting_num_samples),num_rows_d)+1:end,:));

%close all other figures
all_figures = get(0,'Children');
for i = 1:size(all_figures,1)
   if(all_figures(i) > num_figures)
       close(i);
   end
end