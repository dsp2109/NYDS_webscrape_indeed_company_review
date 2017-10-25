from indeed_scrapy.items import IndeedCompanyReview
import scrapy
import pandas as pd

df = pd.read_csv('C:/Users/dsp21/NYDS/Project/Web_Scr_indeed_glassdoor/WebScrapingNYDS_indeed_git/Data/fort500_cmp_url.csv', encoding ='latin1')
df = df['indeed_url']

class indeed_review_spider(scrapy.Spider):
    name = 'indeed_scrapy'
    allowed_urls = ['https://www.indeed.com/']
    start_urls = ['https://www.indeed.com/Best-Places-to-Work?y=2017&cc=US&d=Fortune+500+Companies&start=25']
    #early stage of project (oct17) starting at company review page

    def parse(self, response):

        # ### for top 50 best fort 500 cos to work at
        # url_list = response.xpath('//div[@id = "cmp-curated"]/div[@class = "cmp-company-tile-name"]/a/@href').extract()
        # # SEAN - how would I get page 2 at the same time? Selenium?
        # pageurl = ['https://www.indeed.com' + l for l in url_list]
        # top_list = response.xpath('//div[@id = "cmp-discovery-body"]//h1[@class = "cmp-discovery-title"]/text()').extract_first()

        url_list = df
        pageurl = ['https://www.indeed.com' + l for l in url_list]
        top_list = 'Fortune 500 2017-03-31'

        for url in pageurl[100:]:
            yield scrapy.Request(url, callback=self.parse_company, meta={'top_list':top_list})

    def parse_company(self, response):

        top_list = response.meta['top_list']

        company_name = response.xpath('//div[@id="cmp-name-and-rating"]/div[@class = "cmp-company-name"]/text()').extract_first()
        company_count_salaries = response.xpath('//li[@class = "cmp-menu--salaries"]//div[@class = "cmp-note"]/text()').extract_first()
        company_count_jobs = response.xpath('//li[@class = "cmp-menu--salaries"]//div[@class = "cmp-note"]/text()').extract_first()
        company_count_photos = response.xpath('//li[@class = "cmp-menu--jobs"]//div[@class = "cmp-note"]/text()').extract_first()
        company_count_QnA = response.xpath('//li[@class = "cmp-menu--qna"]//div[@class = "cmp-note"]/text()').extract_first()
        company_indeed_url = response.url
        company_industry = response.xpath('//dl[@id = "cmp-company-details-sidebar"]//a[@data-tn-element= "industryLink"]/text()').extract_first()
        company_hq = response.xpath('//*[@id="cmp-company-details-sidebar"]/dd[1]/text()').extract_first()
        company_rev = response.xpath('//*[@id="cmp-company-details-sidebar"]/dd[2]/text()').extract_first()
        company_empl = response.xpath('//*[@id="cmp-company-details-sidebar"]/dd[3]/text()').extract_first()
        #company_twitter = response.xpath('//h1[@class="timeline-Header-title u-inlineBlock"]/span/a/text()').extract_first()
        #company_facebook = scrapy.Field()
        company_website = response.xpath('//*[@id="cmp-company-details-sidebar"]/dd[5]/a/@href').extract_first()

        company_count_reviews = response.xpath('//div[@class = "cmp-OverallRating"]//div[@class = "cmp-OverallRating-amount"]/text()').extract_first()
        company_count_reviews = int(company_count_reviews.replace(' reviews','').replace(',',''))

        #company agg ratings
        company_overall_rating = response.xpath('//div[@class = "cmp-AtAGlance"]//div[@class = "cmp-OverallRating-average"]/text()').extract_first()
        rating_names = response.xpath('//div[@class = "cmp-AtAGlance"]//span[@class = "cmp-ReviewCategories-name"]/text()').extract()
        rating_name_arr = [None] * 5
        rating_name_arr[:len(rating_names)]= rating_names

        rating_scrs = response.xpath('//div[@class = "cmp-AtAGlance"]//span[@class = "cmp-ReviewCategories-rating"]/text()').extract()
        rating_scr_arr = [None] * 5
        rating_scr_arr[:len(rating_scrs)] = rating_scrs

        rating_name1, rating_name2, rating_name3, rating_name4, rating_name5 = rating_name_arr
        rating_scr1, rating_scr2, rating_scr3, rating_scr4, rating_scr5 = rating_scr_arr

        ceo_approval_pct = response.xpath('//div[@class = "cmp-AtAGlance"]//text[@class = "cmp-PieChart-text"]/text()').extract_first()
        ceo_approval_ratings = response.xpath('//div[@class = "cmp-AtAGlance"]//div[@class = "cmp-CeoApproval-ratings"]/text()').extract_first()

        # work_culture
        bar_names = response.xpath('//div[@class = "cmp-BarChart"]//span[@class = "cmp-BarChart-name"]/text()').extract()
        bar_name_arr = [None] * 5
        bar_name_arr[:len(bar_names)]= bar_names

        bar_pcts = response.xpath('//div[@class = "cmp-BarChart"]//span[@class = "cmp-BarChart-percentage"]/text()').extract()
        bar_pct_arr = [None] * 5
        bar_pct_arr[:len(bar_pcts)] = bar_pcts

        bar_name1, bar_name2, bar_name3, bar_name4, bar_name5 = bar_name_arr
        bar_pct1, bar_pct2, bar_pct3, bar_pct4, bar_pct5 = bar_pct_arr

        item = IndeedCompanyReview()
        item['top_list'] = top_list
        item['company_name'] = company_name
        item['company_count_reviews'] = company_count_reviews
        item['company_count_salaries'] = company_count_salaries
        item['company_count_jobs'] = company_count_jobs
        item['company_count_photos'] = company_count_photos
        item['company_count_QnA'] = company_count_QnA
        item['company_indeed_url'] = company_indeed_url

        item['company_industry'] = company_industry
        item['company_hq'] = company_hq
        item['company_rev'] = company_rev
        item['company_empl'] = company_empl
        # company_twitter 
        # company_facebook
        item['company_website'] = company_website

        item['company_overall_rating'] = company_overall_rating

        item['rating_name1'] = rating_name1
        item['rating_name2'] = rating_name2
        item['rating_name3'] = rating_name3
        item['rating_name4'] = rating_name4
        item['rating_name5'] = rating_name5
        item['rating_scr1'] = rating_scr1
        item['rating_scr2'] = rating_scr2
        item['rating_scr3'] = rating_scr3
        item['rating_scr4'] = rating_scr4
        item['rating_scr5'] = rating_scr5

        item['bar_name1'] = bar_name1
        item['bar_name2'] = bar_name2
        item['bar_name3'] = bar_name3
        item['bar_name4'] = bar_name4
        item['bar_name5'] = bar_name5
        item['bar_pct1'] = bar_pct1
        item['bar_pct2'] = bar_pct2
        item['bar_pct3'] = bar_pct3
        item['bar_pct4'] = bar_pct4
        item['bar_pct5'] = bar_pct5

        item['ceo_approval_pct'] = ceo_approval_pct
        item['ceo_approval_ratings'] = ceo_approval_ratings

        #reviews to iterate through
        review_page_urls = [response.url]
        page_steps = max(company_count_reviews / 5000, 1) #need to limit reviews

        review_page_urls = review_page_urls + \
                          [response.url + '/reviews?fcountry=ALL&start=' + str(int(ls * page_steps * 20)) for ls in range(1, min(250, (company_count_reviews - 1)//20))] #250 pages, 20 reviews = 5000 reviews

        #iterate through review pages
        for url in review_page_urls:
            yield scrapy.Request(url, callback = self.parse_review_page, meta={'item': item})

    def parse_review_page(self, response):
        item_co = response.meta['item']

        reviews = response.xpath('//div[@class = "cmp-review-container"]')
        for review in reviews[1:]:
            item = item_co

            review_title = review.xpath('.//span[@itemprop = "name"]/text()').extract_first()
            reviewer_job_title = review.xpath('.//div[@class = "cmp-review-subtitle"]//span[@class = "cmp-reviewer"]/text()').extract_first()
            reviewer_company_empl_status = review.xpath('.//div[@class = "cmp-review-subtitle"]//span[@class = "cmp-reviewer-job-title"]/text()').extract_first()
            reviewer_job_location = review.xpath('.//div[@class = "cmp-review-subtitle"]//span[@class = "cmp-reviewer-job-location"]/text()').extract_first()
            review_date = review.xpath('.//div[@class = "cmp-review-subtitle"]//span[@class = "cmp-review-date-created"]/text()').extract_first()

            agg_rating = review.xpath('.//span[@class = "cmp-Rating-on"]/@style').extract_first()

            # optional ratings
            ratings = review.xpath('.//table[@class = "cmp-ratings-expanded"]//span[@class = "cmp-Rating-on"]/@style').extract()
            work_life_rating = ratings[0]
            comp_ben_rating = ratings[1]
            jobsec_advancement_rating = ratings[2]
            management_rating = ratings[3]
            culture_rating = ratings[4]

            main_text = review.xpath('.//div[@class = "cmp-review-content-container"]//span[@class = "cmp-review-text"]/text()').extract_first()
            # optional text
            pro_text = review.xpath('.//div[@class = "cmp-review-content-container"]//div[@class = "cmp-review-pro-text"]/text()').extract_first()
            con_text = review.xpath('.//div[@class = "cmp-review-content-container"]//div[@class = "cmp-review-con-text"]/text()').extract_first()

            # optional up/down votes on helpfulness
            helpful_upvote_count = review.xpath('.//div[@class = "cmp-review-vote-report"]//span[@name = "upVoteCount"]/text()').extract_first()
            helpful_downvote_count = review.xpath('.//div[@class = "cmp-review-vote-report"]//span[@name = "downVoteCount"]/text()').extract_first()


            item['review_title'] = review_title

            item['reviewer_job_title'] = reviewer_job_title
            item['reviewer_company_empl_status'] = reviewer_company_empl_status
            item['reviewer_job_location'] = reviewer_job_location
            item['review_date'] = review_date

            item['agg_rating'] = agg_rating

            # optional ratings
            item['work_life_rating'] = work_life_rating
            item['comp_ben_rating'] = comp_ben_rating
            item['jobsec_advancement_rating'] = jobsec_advancement_rating
            item['management_rating'] = management_rating
            item['culture_rating'] = culture_rating

            item['main_text'] = main_text
            # optional text
            item['pro_text'] = pro_text
            item['con_text'] = con_text

            # optional up/down votes on helpfulness
            item['helpful_upvote_count'] = helpful_upvote_count
            item['helpful_downvote_count'] = helpful_downvote_count

            yield item


    #def parse_review(self, response):
        #########
        # for later
        ####


        #
        # app_links = ['https://play.google.com/store/apps/details?id='+ id_ for id_ in app_id]
        #
        # for link in app_links:
        #     yield scrapy.Request(link, callback=self.parse_each)
        #
        # name = response.xpath('//div[@class="id-app-title"]/text()').extract_first()
        # company = response.xpath('//span[@itemprop="name"]/text()').extract_first()
        # category = response.xpath('//span[@itemprop="genre"]/text()').extract_first()
        #
        # reviews = response.xpath('//div[@class="single-review"]')
        #
        # for review in reviews:
        #     content = review.xpath('./div[@class="review-body with-review-wrapper"]/text()').extract()
        #     content = ''.join(content).strip()
        #     rating = review.xpath(
        #         './/div[@class="tiny-star star-rating-non-editable-container"]/@aria-label').extract_first()
        #
        #     item = GooglePlayItem()
        #     item['top_list'] = top_list
        #     item['name'] = name
        #     item['company'] = company
        #     item['content'] = content
        #     item['rating'] = rating
        #     item['category'] = category
        #
        #     yield item
        #
        #
