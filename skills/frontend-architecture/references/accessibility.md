# Accessibility

Use when building or reviewing interactive behavior. Implement accessibility with the feature, not as optional cleanup.

- Start with semantic HTML and native controls: links for navigation, buttons for actions, inputs for entry, and appropriate headings/landmarks. Preserve native keyboard, form, and disabled behavior through wrappers.
- Give controls persistent labels and useful accessible names. Do not use placeholders as labels. Keep visible and accessible names consistent; provide suitable image text or mark decorative images appropriately.
- Ensure every action works by keyboard with logical focus order and visible focus. Do not use positive tabindex to repair DOM order. Implement the complete expected keyboard interaction for a custom widget, using a proven project primitive where possible.
- Manage focus deliberately for dialogs, menus, route changes, removed elements, and submission failures. Restore focus to a meaningful location when closing an overlay. Avoid stealing focus on every state update.
- Use ARIA only when native semantics cannot express the interaction. Keep role, name, state, and keyboard behavior consistent. An ARIA role alone does not make a generic element function as a control.
- Associate instructions and errors with fields. Announce relevant asynchronous outcomes without repeatedly announcing entire screens. Keep error messages actionable beyond color alone.
- Check contrast, zoom, responsive reflow, touch target usability, and non-color state cues. Respect reduced motion while retaining the information an animation communicated.
- Test the changed interaction by keyboard and with existing automated accessibility tools. Use a screen reader when the behavior depends on announcements or complex widget semantics; automated checks alone cannot prove usability.

Use the existing accessible design-system primitives before building a custom widget. Consult official platform or framework documentation for a specialized interaction whose semantics are uncertain.
