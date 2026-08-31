# Eclipse SDV WG TAC RFCs

The "RFC" (request for comments) process provides a consistent and transparent
path for substantial proposals within the responsibilities of the Eclipse
Software Defined Vehicle Working Group Technical Advisory Committee (Eclipse
SDV WG TAC), as described in the charter's [Technical Advisory Committee
section][tac-charter].

This process supplements the [Eclipse SDV Working Group Charter][charter]. It
does not replace the charter, the Eclipse Foundation Working Group Process, or
any other applicable Eclipse Foundation governance document. Those documents
take precedence if they conflict with this process.

Routine corrections and follow-on work can use the normal GitHub pull
request workflow. Substantial proposals should use the RFC process so that TAC
members, Eclipse projects, Project Management Committees (PMCs), and other
stakeholders can understand the proposal and participate in its development.

## Table of Contents

- [When you need to follow this process](#when-you-need-to-follow-this-process)
- [Before creating an RFC](#before-creating-an-rfc)
- [What the process is](#what-the-process-is)
- [After an RFC is accepted](#after-an-rfc-is-accepted)
- [Reviewing RFCs](#reviewing-rfcs)
- [Following up on an RFC](#following-up-on-an-rfc)
- [RFC postponement](#rfc-postponement)
- [Decision-making](#decision-making)
- [Code of Conduct](#code-of-conduct)
- [Contributing](#contributing)
- [Licenses](#licenses)
- [Other policies](#other-policies)

## When you need to follow this process

Use this process for substantial proposals related to the TAC's work. Examples
include significant policies or processes, technical roadmap and coordination
decisions, project-inclusion recommendations, and changes to this RFC process.
The [TAC section of the charter][tac-charter] is the authoritative description
of the committee's scope.

An RFC may develop a proposal that requires action by the Steering Committee,
the Executive Director, the Specification Committee, or another governing
body. Acceptance of such an RFC records the TAC's position or recommendation;
it does not replace any approval required by the charter.

Some changes do not require an RFC:

- editorial corrections and clarifications that do not change meaning;
- routine follow-on work or coordination within an accepted policy or plan;
- project-local technical decisions that remain under the relevant project's
  governance; and
- matters outside the TAC's chartered powers and duties.

If there is uncertainty about whether a proposal needs an RFC, open an issue and
ask before investing in a full proposal.

## Before creating an RFC

A hastily proposed RFC can hurt its chances of acceptance. Before writing one,
discuss the problem with affected projects, PMCs, TAC members, and other
stakeholders. Early discussion helps establish whether the proposal is in scope,
identifies constraints, and exposes alternatives.

RFC authors should document relevant stakeholder input rather than treating the
pull request as the first point of consultation.

An issue in this repository may be used for early discussion. Encouraging
feedback is useful, but it does not guarantee that the RFC will be accepted.

## What the process is

In short, an author proposes a substantial change in a pull request. The TAC and
affected stakeholders review and refine it in public. The TAC then disposes of
the proposal in accordance with the charter. An accepted RFC is merged into the
`text/` directory as the record of that outcome.

1. Fork this repository.
2. Copy `0000-template.md` to `text/0000-my-change.md`, where `my-change` is a
   short descriptive name. Do not assign an RFC number yet.
3. Fill in the RFC. Clearly present the motivation, impact, drawbacks, and
   alternatives.
4. Submit a pull request. Be prepared to revise the RFC in response to review.
5. Once the pull request exists, replace the `0000-` file prefix with the pull
   request number and update the RFC PR field at the top of the file.
6. Build broad support and integrate feedback. The TAC may identify a member to
   help the author find stakeholders, surface constraints, and summarize the
   discussion.
7. Keep substantive discussion in the pull request. Summarize relevant meeting
   or offline discussion there so the public record remains complete.
8. Make revisions visible as new commits while review is active, and leave a
   comment summarizing significant changes. Avoid rebasing or squashing commits
   that reviewers have already seen.
9. When the proposal is ready for a decision, a TAC member may propose a final
   disposition: accept, reject, or postpone. For a lengthy discussion, the
   proposal should include a summary of the tradeoffs and unresolved concerns.
10. Any formal TAC action on the RFC must follow the governance and meeting
    requirements in the charter. The notice period provides a final opportunity
    for affected stakeholders to comment.
11. Material new information may return the RFC to development and defer the
    action.
12. After the TAC acts, the pull request is merged or closed and the disposition
    and rationale are recorded in the pull request.

## After an RFC is accepted

An accepted RFC records a TAC decision or recommendation. Any follow-on actions
may proceed, including obtaining further approval required by the charter or
other governing documents.

Acceptance does not by itself assign priority or ownership to follow-on actions
unless the RFC and the authoritative TAC action explicitly do so. It also does
not transfer authority that belongs to an Eclipse project, PMC, the Steering
Committee, or another governing body.

RFCs should describe the intended outcome accurately, but follow-on work may
expose details that require refinement. Minor corrections can be made in a
follow-up pull request. A substantial change should be proposed as a new RFC
that links to and supersedes or amends the earlier RFC.

## Reviewing RFCs

Review should identify affected projects, PMCs, governing bodies, releases, and
stakeholders. Reviewers should test the proposal against the charter, applicable
Eclipse Foundation processes, the technical roadmap, and existing TAC decisions.

The TAC may discuss an RFC at a meeting or invite the author and affected
stakeholders to participate. A summary of relevant meeting discussion should be
posted to the pull request.

An RFC can be accepted, rejected, or postponed after its benefits, drawbacks,
and constraints are sufficiently understood. If the rationale is not already
clear from the discussion, the final disposition must include it.

## Following up on an RFC

An accepted RFC should identify any follow-on actions and tracking links that
are needed. Some RFCs take effect immediately or record a recommendation and
require no additional work.

Acceptance does not automatically make the RFC author responsible for follow-on
actions or imply that another contributor has been assigned. Coordinate through
the listed tracking links if ownership is unclear.

## RFC postponement

An RFC is postponed when the TAC considers the proposal potentially useful but
defers further consideration or action. The pull request is closed with the
rationale and a `postponed` label. It may be reopened when circumstances change;
no new RFC is required unless the proposal itself changes substantially.

A proposal that is out of scope or that the TAC would not consider in any
foreseeable form should be rejected rather than postponed.

## Decision-making

### Collaboration and rough consensus

The charter states that the TAC discharges its responsibilities through
collaborative evaluation, prioritization, and compromise. RFC review therefore
seeks to understand and address concerns rather than simply count support in the
pull request.

The usual progression is:

1. An RFC presents a proposal and its initial tradeoff analysis.
2. Review identifies additional constraints, drawbacks, and alternatives.
3. The author revises the proposal to address that feedback.
4. Review and revision continue until major concerns are resolved or the
   remaining choice is clear enough for the TAC to decide.

Rough consensus does not require unanimity. It means that relevant perspectives
have been heard, major objections have been considered, and the TAC can make an
informed decision within its chartered authority.

### Formal decisions

The charter's decision-making rules control formal TAC actions. Pull request
reactions, comments, and approvals inform the TAC but do not replace a required
committee action. The final record should identify the meeting or other
authoritative record of the disposition.

### Blocking concerns

A reviewer who believes an RFC should not proceed should describe the concern,
its impact, and reasonable alternatives in the pull request. The author, TAC,
and affected stakeholders should attempt to resolve it during review. If it
cannot be resolved, the concern and competing tradeoffs must be summarized for
the TAC before it acts.

## Code of Conduct

Participation is governed by the [Eclipse Foundation Community Code of
Conduct][code-of-conduct]. Read it before participating so that you understand
the expected standards of behavior and how to report a concern.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## Licenses

Software portions of this repository are available under either the Apache
License, Version 2.0, or the MIT License. Documentation, including RFCs, is
available under the Creative Commons Attribution 4.0 International license.

See [LICENSE-APACHE](LICENSE-APACHE), [LICENSE-MIT](LICENSE-MIT),
[LICENSE-documentation](LICENSE-documentation), and [COPYRIGHT](COPYRIGHT) for
details.

## Other policies

The [Eclipse SDV Working Group Charter][charter] identifies the governing
documents applicable to the Working Group. The [Eclipse Foundation governance
documents][governance-documents] and [legal resources][legal-resources] provide
their current authoritative versions.

[charter]: https://www.eclipse.org/collaborations/working-groups/sdv/charter/
[code-of-conduct]: https://www.eclipse.org/org/documents/Community_Code_of_Conduct.php
[governance-documents]: https://www.eclipse.org/org/documents/
[legal-resources]: https://www.eclipse.org/legal/
[tac-charter]: https://www.eclipse.org/collaborations/working-groups/sdv/charter/#technical-advisory-committee
