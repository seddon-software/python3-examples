<xsl:stylesheet version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

  <xsl:template match="text()">
    <xsl:apply-templates/>
  </xsl:template>

  <xsl:template match="doc">
    <H1>List of Names</H1>
    <xsl:for-each select="name">
      <xsl:value-of select="@last" />,   
      <xsl:value-of select="@first"/>
      <HR/>
    </xsl:for-each>
  </xsl:template>


</xsl:stylesheet>
