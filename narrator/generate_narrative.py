import json
import os

from google import genai
from google.genai import types
from google.colab import userdata

# ==========================================================
# Load Findings
# ==========================================================

def load_findings():

    if os.path.exists("narrator/findings.json"):
        path = "narrator/findings.json"
    else:
        path = "findings.json"   # useful for Colab testing

    with open(path, "r", encoding="utf-8") as file: 
        findings = json.load(file)
    

    return findings


# ==========================================================
# Offline SCR Narrative
# Task 4
# ==========================================================

def generate_scr_narrative_offline(findings: dict) -> dict:

    narrative = f"""
Situation
---------
Mamaearth generated a cleaned total revenue of ₹{findings['cleaned_total_revenue_inr']:.2f}.
The raw SQL revenue was ₹{findings['raw_total_revenue_inr']:.2f}. After removing duplicate
orders, the reconciliation difference was ₹{findings['duplicate_reconciliation_delta_inr']:.2f}.

Complication
------------
Returns are not evenly distributed across payment methods.
Cash on Delivery (COD) has the highest return rate at
{findings['return_rate_by_payment']['COD']}%.

The highest-risk customer segment is COD orders from
Tier-{findings['highest_risk_segment']['city_tier']} cities with a
{findings['highest_risk_segment']['return_rate_pct']}% return rate.

Revenue analysis also showed that January appeared to be the
highest revenue month because of two unusually large bulk
orders. After removing these outliers, the true peak month is
March 2026 with revenue of
₹{findings['true_peak_month']['revenue_inr']:.2f}.

Resolution
----------
Regional operations should prioritize reducing returns in the
COD + Tier-{findings['highest_risk_segment']['city_tier']}
segment. Finance teams should use the cleaned revenue of
₹{findings['cleaned_total_revenue_inr']:.2f} for reporting
instead of the raw revenue because the difference is entirely
explained by duplicate orders rather than genuine business
performance.
"""

    return {
        "status": "success",
        "narrative": narrative,
        "tokens": None
    }


# ==========================================================
# Gemini SCR Narrative
# Task 2 & 3
# ==========================================================

def generate_scr_narrative(findings: dict) -> dict:

    try:
        api_key = userdata.get("APIkey")   # or "GEMINI_API_KEY" if that's your secret name

    except Exception:

        api_key = None


    if not api_key:

        print("No API key found.")
        print("Using Offline Narrative...\n")

        return generate_scr_narrative_offline(findings)

    try:

        client = genai.Client(api_key=api_key)

        system_instruction = """
You are a senior data analyst writing for Mamaearth's
regional operations and finance heads.

Your response MUST contain exactly three sections:

Situation
Complication
Resolution

Rules:

1. Every number must come only from the supplied findings.

2. Do not invent statistics.

3. Do not calculate new numbers.

4. Keep the report professional.

5. Mention all supplied business findings naturally.
"""

        user_prompt = f"""
Write an SCR business narrative using ONLY these verified findings.

Cleaned Revenue:
₹{findings['cleaned_total_revenue_inr']:.2f}

Raw Revenue:
₹{findings['raw_total_revenue_inr']:.2f}

Duplicate Difference:
₹{findings['duplicate_reconciliation_delta_inr']:.2f}

Return Rates:

{findings['return_rate_by_payment']}

Highest Risk Segment:

{findings['highest_risk_segment']}

True Peak Month:

{findings['true_peak_month']}

Outlier Month:

{findings['outlier_inflated_month']}
"""

        # Temperature = 0 because this is a factual business report.
        response = client.models.generate_content(

            model="gemini-3.5-flash-lite",

            contents=user_prompt,

            config=types.GenerateContentConfig(

                system_instruction=system_instruction,

                temperature=0.0,

                max_output_tokens=350,

                http_options=types.HttpOptions(
                    timeout=10000
                )
            )
        )

        narrative = response.text

        tokens = None

        if hasattr(response, "usage_metadata"):

            if response.usage_metadata:

                tokens = response.usage_metadata.total_token_count

        return {

            "status": "success",

            "narrative": narrative,

            "tokens": tokens

        }

    except Exception as err:

        print("\nGemini API failed.")
        print("Switching to Offline Narrative.\n")

        offline = generate_scr_narrative_offline(findings)

        offline["message"] = str(err)

        return offline


# ==========================================================
# Task 5
# Numeric Accuracy Checker
# ==========================================================

def check_numeric_accuracy(narrative):

    print("\n" + "=" * 60)
    print("NUMERIC ACCURACY CHECK")
    print("=" * 60)

    # Remove commas so both "97,358.30" and "97358.30" match
    text = narrative.replace(",", "")

    checks = [

       ("97358.30", ("97358.30" in text) or ("97358.3" in text)),

       ("44.4", "44.4" in text),

       ("54.5", "54.5" in text),

       ("2501.90", ("2501.90" in text) or ("2501.9" in text)),

       ("March",  ("March" in narrative)
          or ("March 2026" in narrative)
          or ("2026-03" in narrative)),

       ("20318.90",("20318.90" in text)
          or ("20318.9" in text))
    ]

    for label, passed in checks:

        if passed:

            print(f"PASS : {label}")

        else:

            print(f"FAIL : {label}")

# ==========================================================
# Main Program
# ==========================================================

def main():

    print("=" * 60)
    print("MAMAEARTH RETURNS & GROWTH INTELLIGENCE NARRATOR")
    print("=" * 60)

    findings = load_findings()

    result = generate_scr_narrative(findings)

    print("\nStatus :", result["status"])

    if result["status"] == "success":

        print("\n" + "=" * 60)
        print("SCR NARRATIVE")
        print("=" * 60)

        print(result["narrative"])

       # Check whether narrator folder exists
        if os.path.exists("narrator"):
           sample_output_path = "narrator/sample_output.txt"

        else:
           # Create narrator folder if it doesn't exist
           os.makedirs("narrator")
           sample_output_path = "narrator/sample_output.txt"

           # Save narrative
        with open(sample_output_path, "w", encoding="utf-8") as f:
            f.write(result["narrative"])


        # Read saved narrative
        with open(sample_output_path, "r", encoding="utf-8") as f:
           saved_output = f.read()
       
        # Run checker on saved output
        check_numeric_accuracy(saved_output)

    else:
      
        print("\nNarrative Generation Failed")
        print(result["message"])

    


if __name__ == "__main__":

    main()

