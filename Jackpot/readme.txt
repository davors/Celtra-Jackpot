														
														
binary distribution sampling accuracy, required number of repeats to achive an 95% confidence interval of...
	//20000, 95% confidence that true value deviates less by 1%
	//5000,  95% confidence that true value deviates less by 2%
	//1200,  95% confidence that true value deviates less by 4%
	//750,   95% confidence that true value deviates less by 5% (default setting)
	//200,	 95% confidence that true value deviates less by 10%
	
	
//calculate the confidence, that two samples belong to different normal distributions
confidence_normal_dist1 =
	sqrt(
		(sample2_num_repeats)
		* (sample1 - sample2) * (sample1 - sample2)
		/ (sample2 * (1-sample2) + 0.00001)	// + 0.00001 only to avoid division by 0
		/ 2.0 //optional
	);
//calculate the confidence, that the last two scores belong to different normal distributions
confidence_normal_dist2 =
	sqrt(
		(sample1_num_repeats)
		* (sample1 - sample2) * (sample1 - sample2)
		/ (sample1 * (1-sample1) + 0.00001)	// + 0.00001 only to avoid division by 0
		/ 2.0 //optional
	);

	Possible algorithms:
	UCB1
	UCB1-TUNED
	Epsilon_n GREEDY 
	http://lane.compbio.cmu.edu/courses/slides_ucb.pdf
	http://www.cs.mcgill.ca/~vkules/bandits.pdf
	http://www.cs.cmu.edu/~deepay/mywww/papers/nips08-mortal.pdf
	http://hal.inria.fr/docs/00/16/40/33/PDF/cap07.pdf






