# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class IndeedCompanyReview(scrapy.Item):
    # this Item will record a review of a company by a reviewer who claims to be an an employee, on indeed.com:
    # should follow up by scraping company specific data like number of reviews, agg rating, salaries

    top_list = scrapy.Field()

    #company fields. SEAN - can this be counted at a higher level?
    company_name = scrapy.Field()
    company_count_reviews = scrapy.Field()
    company_count_salaries = scrapy.Field()
    company_count_jobs = scrapy.Field()
    company_count_photos = scrapy.Field()
    company_count_QnA = scrapy.Field()
    company_indeed_url = scrapy.Field()

    company_rev = scrapy.Field()
    company_empl = scrapy.Field()
    company_industry = scrapy.Field()
    company_hq = scrapy.Field()
    company_twitter = scrapy.Field()
    company_facebook = scrapy.Field()
    company_website = scrapy.Field()




    company_overall_rating = scrapy.Field()
    rating_name1 = scrapy.Field()
    rating_scr1 = scrapy.Field()
    rating_name2 = scrapy.Field()
    rating_scr2 = scrapy.Field()
    rating_name3 = scrapy.Field()
    rating_scr3 = scrapy.Field()
    rating_name4 = scrapy.Field()
    rating_scr4 = scrapy.Field()
    rating_name5 = scrapy.Field()
    rating_scr5 = scrapy.Field()

    ceo_approval_pct = scrapy.Field()
    ceo_approval_ratings = scrapy.Field()

    #work_culture
    bar_name1 = scrapy.Field()
    bar_pct1 = scrapy.Field()
    bar_name2 = scrapy.Field()
    bar_pct2 = scrapy.Field()
    bar_name3 = scrapy.Field()
    bar_pct3 = scrapy.Field()
    bar_name4 = scrapy.Field()
    bar_pct4 = scrapy.Field()
    bar_name5 = scrapy.Field()
    bar_pct5 = scrapy.Field()

    review_title = scrapy.Field()
    reviewer_job_title = scrapy.Field()
    reviewer_company_empl_status = scrapy.Field()
    reviewer_job_location = scrapy.Field()
    review_date = scrapy.Field()



    agg_rating = scrapy.Field()
    # optional ratings
    work_life_rating = scrapy.Field()
    comp_ben_rating = scrapy.Field()
    jobsec_advancement_rating = scrapy.Field()
    management_rating = scrapy.Field()
    culture_rating = scrapy.Field()

    main_text = scrapy.Field()
    #optional text
    pro_text = scrapy.Field()
    con_text = scrapy.Field()

    # optional up/down votes on helpfulness
    helpful_upvote_count = scrapy.Field()
    helpful_downvote_count = scrapy.Field()