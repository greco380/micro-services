# Recurring Income Planner Service

A practical, assumptions-based helper to choose which microservice idea to build first when your goal is to reach **~€400/month profit** from a small starting budget.

> ⚠️ Important: no tool can guarantee fixed monthly returns. This service helps you make better decisions, reduce risk, and pick the fastest path to a realistic target.

## Why this exists

If you have around **€100** to invest, the best strategy is usually to build a **small B2B micro-SaaS** that:
- solves one painful workflow,
- charges monthly,
- is cheap to host,
- can be sold repeatedly.

This service ranks ideas based on estimated:
- monthly profit,
- payback period,
- confidence/risk,
- required maintenance time.

## Recommended first project

Based on the sample assumptions in `opportunities.sample.json`, the suggested first build is:

### **Invoice Follow-up and Payment Nudges**

A microservice that helps freelancers and small agencies automatically:
- detect overdue invoices,
- send polite reminder sequences (email + optional WhatsApp/SMS),
- escalate reminders to managers,
- log communication history for accounting.

Why this is a strong pick for your €400/month goal:
- Clear ROI for clients (faster payments).
- Easy to explain and sell locally.
- Low infrastructure cost.
- Sticky recurring usage.

## Minimal monetization model

- **Starter plan**: €29/month (up to 30 reminders)
- **Pro plan**: €45/month (automation + templates)
- **Agency plan**: €79/month (multi-client workspace)

Example path to €400/month:
- 10 clients on Pro (€45) = €450 revenue
- ~€25 infra/tools = ~€425 estimated monthly profit

## Run the scorer

```bash
cd recurring-income-planner
python3 opportunity_scorer.py --input opportunities.sample.json --target-profit 400
```

## Implementation roadmap

1. **Week 1**: Build webhook/API intake for invoices and reminders queue.
2. **Week 2**: Add email templates, retry logic, and audit logs.
3. **Week 3**: Stripe subscriptions + simple admin dashboard.
4. **Week 4**: Onboard first 3 pilot users and collect testimonials.

## Validation checklist (before coding more)

- Talk to 15 target users (freelancers/agencies/SMBs).
- Confirm at least 5 currently chase overdue invoices manually.
- Pre-sell 3 pilots at discounted monthly pricing.
- Only then scale features.

The fastest path to consistent profit is not feature count — it's solving one expensive problem repeatedly.
