module DigitalRoot (digitalRoot) where

digitalRoot :: Integral a => a -> a
-- convert an integer to a sum of the digits

digitalRoot n
    | 9 < n = digitalRoot(sum(digs n))
    | 0 <= n = n
    | otherwise = error "Invalid input"

digs :: Integral x => x -> [x]
digs 0 = []
digs x = digs (x `div` 10) ++ [x `mod` 10]

-- digitalRoot :: Integral a => a -> a
-- digitalRoot 0 = 0
-- digitalRoot n = 1 + (n - 1) `mod` 9