# Changelog

## [0.6.1](https://github.com/tembo/sdk-python/compare/v0.6.0...v0.6.1) (2026-10-29)


### Chores

* **api:** update generated SDK content ([16996d7](https://github.com/tembo/sdk-python/commit/16996d7e4e0484f5cdb2a989f9f33e632fa7d33b))

## [0.6.0](https://github.com/tembo/sdk-python/compare/v0.5.0...v0.6.0) (2026-10-28)


### ⚠ BREAKING CHANGES

* **api:** 3 breaking changes to the SDK surface.
    - Removed operation `organizations.subscriptions.reset` (`POST /v1/organizations/{organizationId}/subscriptions/reset`).
    - Removed operation `users.delete` (`DELETE /v1/users/{userId}`).
    - Removed operation `users.subscriptions.reset` (`POST /v1/users/{userId}/subscriptions/reset`).

### Features

* **api:** update SDK surface (10 changes) ([c77633b](https://github.com/tembo/sdk-python/commit/c77633b90e182d6d7b0d279410d6b82e436872ca))
* **api:** update SDK surface (3 changes) ([aecec17](https://github.com/tembo/sdk-python/commit/aecec170fe9b4bc13722dadbdbc08e9b662b2f90))

## [0.5.0](https://github.com/tembo/sdk-python/compare/v0.4.0...v0.5.0) (2026-10-23)


### ⚠ BREAKING CHANGES

* **api:** Schema `agent_options_input` shape changed.

### Features

* **api:** update schema agent_options_input (+7 more changes) ([1284046](https://github.com/tembo/sdk-python/commit/1284046585d20374b6f94c05393ed468bf45a5b4))

## [0.4.0](https://github.com/tembo/sdk-python/compare/v0.3.0...v0.4.0) (2026-10-21)


### Features

* **api:** add operation sessions.inputs.list (+3 more changes) ([388c5f4](https://github.com/tembo/sdk-python/commit/388c5f4809a80a985a41cf4f7ad5a4fdcefbedce))
* **api:** update SDK surface (2 changes) ([5a169ec](https://github.com/tembo/sdk-python/commit/5a169ec1541810a30e8f778148b80b593e6c62d2))

## [0.3.0](https://github.com/tembo/sdk-python/compare/v0.2.0...v0.3.0) (2026-10-19)


### Features

* **api:** initial SDK generation ([b356bfb](https://github.com/tembo/sdk-python/commit/b356bfbc4f5b4218bc0290955c74c86aac68e9d4))


### Bug Fixes

* **types:** break TipTapNode circular import ([692a44e](https://github.com/tembo/sdk-python/commit/692a44e5b4c4c13a22676a0db206bce3a252238b))
* **types:** break TipTapNode circular import ([fafebb9](https://github.com/tembo/sdk-python/commit/fafebb93930acba8f39c39ba08c4a5be82020e60))

## 0.2.0 (2026-01-05)

Full Changelog: [v0.1.0...v0.2.0](https://github.com/tembo/sdk-python/compare/v0.1.0...v0.2.0)

### Features

* **api:** api update ([ec8177b](https://github.com/tembo/sdk-python/commit/ec8177b069c4f04a6a525ae831aea5cd21411e66))
* **api:** api update ([c13ae2a](https://github.com/tembo/sdk-python/commit/c13ae2a7df6d479fc2010a93ef4f97e4bba45743))

## 0.1.0 (2025-11-30)

Full Changelog: [v0.0.1...v0.1.0](https://github.com/tembo/sdk-python/compare/v0.0.1...v0.1.0)

### Features

* **api:** manual updates ([7b8903f](https://github.com/tembo/sdk-python/commit/7b8903f0edba052f2419aeab123d5afd016169a8))


### Bug Fixes

* ensure streams are always closed ([d2ce3dc](https://github.com/tembo/sdk-python/commit/d2ce3dc9c8d7e7f6872effe457b159535c3f87b0))


### Chores

* add docs link ([76a2db3](https://github.com/tembo/sdk-python/commit/76a2db33d4571b163218d228210f972ce55c6842))
* **deps:** mypy 1.18.1 has a regression, pin to 1.17 ([1210f2d](https://github.com/tembo/sdk-python/commit/1210f2d0c5d25ea24e207ce1d0a6cc8329a4771b))
* update SDK settings ([bf72b87](https://github.com/tembo/sdk-python/commit/bf72b87e5b910cc8c9e41c79f27b689ea9a87132))
* update SDK settings ([d867308](https://github.com/tembo/sdk-python/commit/d86730803bf8cafa9f43719f233ed8d1888f63d7))
