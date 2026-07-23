# Example Prompts

## Turn an Article into a Presentation

```text
Please use the codex-ppt skill to turn /path/to/article.md into a Chinese presentation of about 10 slides. The audience is an internal technical team.
```

## Turn a Paper into a Thesis Defense Presentation

```text
Please use the codex-ppt skill to turn this paper into a 12-slide Chinese thesis defense presentation. Use a scientific defense style. The structure should cover the research background, method, experiments, results, limitations, and conclusion. Preserve the model architecture diagram and the main experiment result figures from the paper on the corresponding slides.
```

## Specify a Visual Style

```text
Please use the codex-ppt skill to generate a presentation. Use the PDF I uploaded as the visual style reference: large titles, generous whitespace, a black-white-gray palette, and small red accents, with the overall feel of a business magazine feature. Review every page image in the material in detail to understand its style, then generate the presentation in a similar style.
```

## Specify a Built-in Style

```text
Please use the codex-ppt skill to turn this material into a 10-slide presentation. Use the built-in "Hand-Drawn Technical Explanation" style, with hand-drawn lines, structured diagrams, lightweight annotations, and clear concept breakdowns. It should be suitable for explaining technical principles and popularizing knowledge.
```

You can also replace the style name with another built-in option such as "Clean Professional," "Scientific Defense," "Data Dashboard," "E-Ink Magazine," or "Creative Magazine."

## Specify the Slide Count and Source Materials

```text
Please use the codex-ppt skill to turn this material into a 15-slide presentation. Use architecture.png on slide 4 and benchmark-results.png on slide 9.
```

## Revise One Slide

```text
Slide 6 is too dense, and its title is not clear enough. Regenerate only slide 6, preserve the style of the complete presentation, and reorganize the content into a clearer three-part structure.
```

## Save a Style to the Personal Style Library

```text
I really like the visual style of this presentation. Save it to the codex-ppt personal style library for future reuse. Include the color palette, typographic character, layout rules, illustration/chart style, and suitable use cases in the description.
```
