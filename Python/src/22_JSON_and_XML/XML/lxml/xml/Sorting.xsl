<xsl:stylesheet version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

  <xsl:template match="doc">
    <H1>Sorted List of Names</H1>
    <xsl:for-each select="name">
      <xsl:sort select="@last" order="ascending" />
      <xsl:value-of select="@last" />,
      <xsl:value-of select="@first"/>
      <HR/>
    </xsl:for-each>
  </xsl:template>


</xsl:stylesheet>
