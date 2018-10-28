#!/bin/bash
for i in {1..30}
	do
		HTML="https://www.amazon.com/Gardens-Moon-Malazan-Book-Fallen/product-reviews/0765348780/ref=cm_cr_getr_d_paging_btm_${i}?ie=UTF8&filterByStar=five_star&reviewerType=avp_only_reviews&pageNumber=${i}#reviews-filter-bar"
		curl $HTML | sed 's/\(<span data-hook="review-body" class="a-size-base review-text">\)/\n\1/g' > temp1.txt
		cat temp1.txt | sed 's/<\/span>/\n/g' > temp2.txt
		cat temp2.txt | grep '<span data-hook="review-body" class="a-size-base review-text">'  > temp3.txt
		cat temp3.txt | sed 's/<span data-hook="review-body" class="a-size-base review-text">/\n****/g' | sed 's/<br \/>/\n/g' > temp4.txt
		cat temp4.txt >> result.txt
		echo ${i} is done
	done