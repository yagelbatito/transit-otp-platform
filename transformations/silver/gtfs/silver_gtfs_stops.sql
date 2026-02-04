-- silver_gtfs_stops.sql
-- Purpose:
-- Silver layer table for GTFS stops, filtered to Yeruham only.

-- Source:
-- Bronze GTFS stops.txt

-- Columns to keep:
-- stop_id
-- stop_name
-- stop_lat
-- stop_lon

-- Filtering logic:
-- Keep only stops where stop_name contains 'ירוחם'
-- (Later we may replace this with geographic bounding box)
