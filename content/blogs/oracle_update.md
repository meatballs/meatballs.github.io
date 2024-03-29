---
title: Oracle Update Statements
date: 2012-03-08
tags: [Oracle, SQL]
---
There are several methods in Oracle SQL to update records in one table based on the content of another table.

Here, I give some of those methods and some guidance on where they might be most appropriate.

## The Basics

Oracle uses a 'correlated subquery' syntax which looks like this:

```
UPDATE  target t
SET t.column = s.column
(SELECT
FROM  source s
WHERE s.join_column = t.join_column)
```

The bracketed subquery joins the source and target tables and the target table is updated with values from the source column. I've shown a simple join between the two tables using one column from each, but the WHERE clause in the subquery can be as complex as required.

## NULLs

The basic syntax I've given above assumes that there is one, and only one, matching record in the source table for each target record.

If there are records in the target table with no matching source record, Oracle will return a 'Cannot update to null' error. In other words, if it can't find a matching record in the source table (according to whatever join criteria have been used), then how can it know the value to update the target record?

There are several ways to deal with this problem:

## A WHERE Clause

The simplest method is to limit the set of target records which are to be updated:

```
UPDATE  target t
SET t.column = s.column
(SELECT
FROM  source s
WHERE s.join_column = t.join_column)
WHERE t.column......
```

Above, I've added a simple WHERE clause to the main query (not to be confused with the WHERE clause in the subquery which joins the two tables). This simply applies a criterion to some column on the target table and limits the update to those records which meet the criterion.

## The NVL function

It's not always possible to determine in advance the set of records to be updated. Often, we want to update those target records which have a matching source record and that can be a dynamic set. One simple method uses the NVL function which allows us to make a substitution when a NULL value is encountered. Here's some example code:

```
UPDATE  target t
SET t.column = s.column
NVL((SELECT
FROM  source s
WHERE s.join_column = t.join_column),)
```

This code wraps the subquery inside the NVL function so that any target records without matching source records will be updated to their current content. In other words, all matching records will be updated to the value from the source table, all other records will remain the same.

It's worth noting that in this example, every record in the target table still updated. It's just that some of them will be updated to the same value that they already contained. This can be inefficient if only a small percentage of the target records are matched.

## WHERE EXISTS

It's possible to limit the target records to precisely those matched in the source table by using the WHERE EXISTS syntax:

```
UPDATE  target t
SET t.column = s.column
(SELECT
FROM  source s
WHERE s.join_column = t.join_column)
WHERE EXISTS
(SELECT *
FROM  s
WHERE s.join_column = t.join_column)
```

This is a more complex WHERE clause than the earlier simple example, but it's the same idea; we're using a WHERE clause to limit the set of target records to be affected by the UPDATE.

I've shown the join in the WHERE EXISTS clause to be identical to that in the original subquery. This means that the target set is limited precisely to those matching records. However, there is no reason why the EXISTS join should not return a different set, if required. If it returns a subset, it merely limits the target set further. If it returns more records than the matched set, then those null values would have to be dealt with using further WHERE clauses or the NVL function (or both!!).

Whether the NVL function or the WHERE EXISTS method is more efficient depends entirely upon the nature and circumstances of your application (e.g. the absolute and relative size of the tables, the complexity of the joins, the uniqueness of the records, the existence of indexes). It is well worthwhile to try both and to look at the execution plan before settling on a preferred solution.

## Inline Views

This is possibly my favourite method!! Although I normally try more than one solution and use the execution plan to determine my preference, it's rare that any other method beats the inline view for efficiency.

The idea here is that we update a view rather than a table. Any joins or limitations on the set to update are performed in the view:

```
UPDATE
(SELECT t.column, s.column
FROM  target t,  source s
WHERE s.join_column = t.join_column)
SET t.column = s.column
```

There are some restrictions on whether Oracle will allow tables to be updated via a view. Essentially, each row in the view must map to one and only one record in the underlying target table or, to put it in the more common jargon, the primary key of the target table must be preserved in the view.
