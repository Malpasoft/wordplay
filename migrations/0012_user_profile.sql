-- Learner profile fields used to personalise the dashboard course navigator.
-- l1 = native language; target_lang = language they want to learn.
ALTER TABLE users ADD COLUMN l1 TEXT;
ALTER TABLE users ADD COLUMN target_lang TEXT;
ALTER TABLE users ADD COLUMN goal TEXT;
