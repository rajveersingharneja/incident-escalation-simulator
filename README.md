# Incident Escalation Simulator

This project simulates how backend systems decide whether an issue is serious enough to escalate to humans or whether it is safer to continue observing.

The focus is not on detecting failures or predicting outages, but on understanding how escalation decisions behave when incoming signals are noisy, delayed, duplicated, or incomplete.

---

## Why this project

In real production systems, errors happen constantly.

Some resolve on their own.  
Some are temporary.  
Some grow into real incidents.

If a system escalates too quickly, engineers experience alert fatigue and stop trusting notifications.  
If it escalates too slowly, genuine incidents are detected late.

This project explores how escalation logic behaves under uncertainty and how different decision philosophies trade responsiveness for stability.

---

## What is being simulated

The simulator represents an internal incident monitoring setup inside a tech company.

Multiple services (for example checkout, payments, authentication) emit signals such as:

- warnings  
- error spikes  
- recovery messages  

These signals are intentionally unreliable. Events may arrive late, be duplicated, or be dropped entirely, reflecting real distributed system behavior.

---

## System flow

- Services emit incident events  
- Events pass through an unreliable delivery layer  
- Recent history is stored per service  
- Escalation decisions are made based on patterns over time  

The system produces one of three outcomes:

- **WAIT** — insufficient or unstable evidence  
- **MONITOR** — elevated activity detected  
- **ESCALATE** — strong and persistent signals  

Escalation is intentionally rare.

---

## Escalation policies considered

Different escalation philosophies behave very differently under noisy conditions.

This simulator is designed to reason about three common approaches:

- **Immediate escalation**  
  Escalate on the first error signal.

- **Threshold-based escalation**  
  Escalate after a fixed number of errors within a short time window.

- **Conservative confirmation-based escalation (implemented)**  
  Escalate only when errors persist over time, recovery signals do not dominate, and cooldown constraints are satisfied.

The current implementation follows the conservative policy, while the simulator allows behavioral comparison against more aggressive alternatives under the same uncertain event stream.

---

## Evaluation metrics

Rather than prediction accuracy, the system is evaluated using behavioral metrics:

- escalation count  
- frequency of decision changes (alert churn)  
- tendency toward false escalation  
- escalation delay after first error  

These metrics help characterize how different policies balance responsiveness against stability.

---

## Observations

Running the simulator highlights clear trade-offs.

Aggressive escalation strategies react quickly but generate frequent false positives when errors are transient or recovery signals arrive slightly late.

More conservative strategies significantly reduce alert volume and decision churn, but introduce longer escalation delays during genuine incidents.

This reflects a fundamental tension in incident management systems:  
**responsiveness versus stability under uncertainty.**

No single policy is universally optimal — escalation behavior must be chosen based on tolerance for alert fatigue versus delayed response.

---

## Design approach

The system intentionally uses rule-based logic rather than predictive models.

This keeps decisions interpretable and allows clear reasoning about why an escalation occurred or did not occur.

The goal is not to maximize sensitivity, but to study how system behavior changes under unreliable signal delivery.

---

## Running the simulation

Install dependencies:

```bash
pip install -r requirements.txt
python main.py
