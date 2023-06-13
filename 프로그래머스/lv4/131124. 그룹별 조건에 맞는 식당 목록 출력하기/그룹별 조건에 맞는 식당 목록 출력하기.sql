-- 코드를 입력하세요
SELECT M.member_name, R.review_text, date_format(R.review_date, "%Y-%m-%d")
from member_profile M
join (
        select review_text, review_date, member_id
        from rest_review
        where member_id = (
        select member_id
        from rest_review
        group by member_id
        order by count(*) desc
        limit 1)
        ) R
on R.member_id = M.member_id
order by R.review_date, R.review_text;