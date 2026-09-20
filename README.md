# Gumroad Template Opportunity Agent

A research-first agent for discovering, evaluating, and developing digital-template opportunities.

## Mission

Find template-product opportunities, research them with traceable evidence, turn promising opportunities into practical bundles and listings, and stop at a human-review gate.

## Hard safety boundary

This project creates research, evidence records, opportunity assessments, draft bundles, draft listings, and human-review packets. It deliberately has no Gumroad publishing capability. Publishing must remain an explicit human action outside this pipeline.

The agent must not invent market demand, sales, revenue, rankings, customer counts, testimonials, or other unsupported claims. Guesses belong in assumptions. Absolute, guaranteed, and quantitative claims are flagged for review.

## Pipeline

research -> evidence normalization -> opportunity scoring -> bundle drafting -> claim audit -> review packet -> HUMAN APPROVAL

The score is a research-prioritization heuristic. It is not a sales forecast or probability of success.

## Current implementation

The repository contains typed models for opportunities and evidence, evidence validation and transparent scoring, claim auditing, deterministic bundle/listing generation, a CLI, tests, and an agent specification with forbidden actions.

The research/discovery layer is provider-neutral. Search adapters should feed normalized Evidence objects while preserving the source URL and actual observation. This prevents an uncited research blob from becoming fake certainty.

## Run

python -m agent.cli examples/opportunity.json --out review-packet.json

The example uses placeholder evidence and must not be treated as real market research.

## Test

python -m pytest
