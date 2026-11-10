"""
RJMedia Video Data Manager
Loads your YouTube channel data from Google Sheets CSV export
Makes it easy to update videos without touching code
"""

import pandas as pd
import json
from datetime import datetime

# Sample data extracted from your spreadsheet
# In production, this would read from Google Sheets API or CSV

CHANNEL_DATA = {
    "total_views": 967422,
    "total_watch_hours": 68056.5,
    "total_subscribers": 1891,
    "avg_ctr": 4.55,
    "videos": [
        {
            "id": "WLU74h889VI",
            "title": "The Smiths - live Rockabilly 1984 FHD",
            "artist": "The Smiths",
            "date": "May 5, 2025",
            "views": 14994,
            "watch_hours": 12711.72,
            "subscribers": 299,
            "estimated_revenue_gbp": 0,
            "thumbnail_impressions": 1285774,
            "ctr": 3.58,
            "url": "https://www.youtube.com/watch?v=WLU74h889VI"
        },
        {
            "id": "...",
            "title": "Peter Green (Fleetwood Mac) - 1997 Documentary Discussing LSD and giving money away.",
            "artist": "Peter Green",
            "date": "Jul 17, 2024",
            "views": 179079,
            "watch_hours": 21134.01,
            "subscribers": 598,
            "estimated_revenue_gbp": 0,
            "thumbnail_impressions": 3592939,
            "ctr": 3.35,
            "url": "https://www.youtube.com/watch?v=..."
        },
        {
            "id": "...",
            "title": "The Buzzcocks - What Do I Get (Live Softest 2021)",
            "artist": "The Buzzcocks",
            "date": "Aug 30, 2021",
            "views": 225097,
            "watch_hours": 9380.97,
            "subscribers": 276,
            "estimated_revenue_gbp": 0,
            "thumbnail_impressions": 13950376,
            "ctr": 4.55,
            "url": "https://www.youtube.com/watch?v=..."
        },
        {
            "id": "...",
            "title": "Everton 3-2 Crystal Palace - 1982 May Match - Calvert-Lewin goal",
            "artist": "Sports Archive",
            "date": "May 11, 2022",
            "views": 19194,
            "watch_hours": 1585.33,
            "subscribers": 104,
            "estimated_revenue_gbp": 0,
            "thumbnail_impressions": 1617753,
            "ctr": 10.0,
            "url": "https://www.youtube.com/watch?v=..."
        },
        {
            "id": "...",
            "title": "Peter Green : A Hard Road",
            "artist": "Peter Green",
            "date": "Jun 11, 2023",
            "views": 90131,
            "watch_hours": 10006.78,
            "subscribers": 253,
            "estimated_revenue_gbp": 0,
            "thumbnail_impressions": 1508559,
            "ctr": 3.91,
            "url": "https://www.youtube.com/watch?v=..."
        },
        {
            "id": "...",
            "title": "Mansun - Glastonbury 1998 Full Set",
            "artist": "Mansun",
            "date": "Jun 25, 2023",
            "views": 21846,
            "watch_hours": 6900.71,
            "subscribers": 6,
            "estimated_revenue_gbp": 0,
            "thumbnail_impressions": 30882,
            "ctr": 5.61,
            "url": "https://www.youtube.com/watch?v=..."
        },
        {
            "id": "...",
            "title": "Jesus and Mary Chain - Jamcod live Manchester Albert Hall 23/03/2024",
            "artist": "Jesus and Mary Chain",
            "date": "Mar 24, 2024",
            "views": 5347,
            "watch_hours": 161.89,
            "subscribers": 11,
            "estimated_revenue_gbp": 0,
            "thumbnail_impressions": 40800,
            "ctr": 8.33,
            "url": "https://www.youtube.com/watch?v=..."
        },
        {
            "id": "...",
            "title": "Kasabian - L.S.F.",
            "artist": "Kasabian",
            "date": "Feb 22, 2024",
            "views": 28480,
            "watch_hours": 1053.92,
            "subscribers": 34,
            "estimated_revenue_gbp": 0,
            "thumbnail_impressions": 230453,
            "ctr": 7.62,
            "url": "https://www.youtube.com/watch?v=..."
        },
    ]
}

def get_channel_data():
    """Return full channel data"""
    return CHANNEL_DATA

def get_videos_sorted(sort_by="watch_hours", reverse=True):
    """Get videos sorted by specified field"""
    videos = CHANNEL_DATA["videos"].copy()
    return sorted(videos, key=lambda x: x[sort_by], reverse=reverse)

def get_top_videos(n=10):
    """Get top N videos by watch hours"""
    return get_videos_sorted("watch_hours", reverse=True)[:n]

def calculate_tip_potential(views, conversion_rate=0.01, tip_amount=2):
    """Calculate estimated tip income"""
    return int(views * conversion_rate * tip_amount)

def get_monetization_scenarios():
    """Return monetization scenarios"""
    total_views = CHANNEL_DATA["total_views"]
    
    return {
        "conservative": {
            "name": "0.5% tip rate @ £1",
            "rate": 0.005,
            "amount": 1,
            "annual": int(total_views * 0.005 * 1),
        },
        "moderate": {
            "name": "1% tip rate @ £2",
            "rate": 0.01,
            "amount": 2,
            "annual": int(total_views * 0.01 * 2),
        },
        "optimistic": {
            "name": "2% tip rate @ £2.50",
            "rate": 0.02,
            "amount": 2.5,
            "annual": int(total_views * 0.02 * 2.5),
        },
    }

def search_videos(query):
    """Search videos by title or artist"""
    query = query.lower()
    return [v for v in CHANNEL_DATA["videos"] if query in v["title"].lower() or query in v["artist"].lower()]

def export_to_csv():
    """Export video data as CSV"""
    df = pd.DataFrame(CHANNEL_DATA["videos"])
    return df.to_csv(index=False)

if __name__ == "__main__":
    # Test data
    print("Total Videos:", len(CHANNEL_DATA["videos"]))
    print("Top Video:", get_top_videos(1)[0]["title"])
    print("Monetization Scenario:", get_monetization_scenarios()["moderate"])
