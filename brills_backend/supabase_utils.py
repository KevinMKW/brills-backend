from supabase_py import create_client
import json

SUPABASE_URL = "https://krqxlsjfucljkcfezdfu.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImtycXhsc2pmdWNsamtjZmV6ZGZ1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDU0MTU4NzYsImV4cCI6MjAyMDk5MTg3Nn0.KtvldXKdDs1wn0v3V4pytKl0twMscBgSFWNrNnAEpdE"

def create_supabase_client():
    return create_client(SUPABASE_URL, SUPABASE_KEY)

def send_magic_link(email):
    supabase = create_supabase_client()

    # Generate magic link
    magic_link_response = supabase.auth.create_magic_link(email)

    # Extract the magic link from the response
    magic_link = json.loads(magic_link_response.content)["data"]["magic_link"]

    # Send the magic link to the user (e.g., via email)

    return magic_link
