-- 코드를 입력하세요
SELECT P.product_code, sum(O.sales_amount * P.price) as sales
from product P
join offline_sale O
on P.product_id = O.product_id
group by P.product_code
order by sales desc, P.product_code asc;