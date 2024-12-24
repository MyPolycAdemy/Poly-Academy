# Generated by Django 5.1.3 on 2024-12-23 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_rename_class_model_classcontentmodel_class_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='classcontentmodel',
            name='audio',
            field=models.FileField(blank=True, null=True, upload_to='content_audios/'),
        ),
        migrations.AddField(
            model_name='classcontentmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='content_images/'),
        ),
        migrations.AddField(
            model_name='classcontentmodel',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='content_pdfs/'),
        ),
        migrations.AddField(
            model_name='classcontentmodel',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='content_videos/'),
        ),
        migrations.AlterField(
            model_name='classcontentmodel',
            name='content_type',
            field=models.CharField(choices=[('multiple_choice', 'Multiple Choice'), ('true_false', 'True or False'), ('fill_gaps', 'Fill in the Gaps'), ('word_bank', 'Word Bank'), ('drop_down_text', 'Drop Down Text'), ('ordering', 'Ordering'), ('sorting', 'Sorting'), ('category', 'Category'), ('matching', 'Matching'), ('flashcards', 'Flashcards'), ('table', 'Table'), ('accordion', 'Accordion'), ('tabs', 'Tabs'), ('button_stack', 'Button Stack'), ('process', 'Process'), ('timeline', 'Timeline'), ('multiple_choice_knowledge_check', 'Multiple Choice Knowledge Check'), ('true_false_knowledge_check', 'True or False Knowledge Check'), ('fill_gaps_knowledge_check', 'Fill in the Gaps Knowledge Check'), ('word_bank_knowledge_check', 'Word Bank Knowledge Check'), ('drop_down_text_knowledge_check', 'Drop Down Text Knowledge Check'), ('ordering_knowledge_check', 'Ordering Knowledge Check'), ('sorting_knowledge_check', 'Sorting Knowledge Check'), ('categories_knowledge_check', 'Categories Knowledge Check'), ('matching_knowledge_check', 'Matching Knowledge Check'), ('word_order_knowledge_check', 'Word Order Knowledge Check'), ('picture_matching_knowledge_check', 'Picture Matching Knowledge Check'), ('picture_labeling_knowledge_check', 'Picture Labeling Knowledge Check'), ('text_block', 'Text Block'), ('text_article', 'Text Article'), ('text_quote', 'Text Quote'), ('text_highlighted', 'Text Highlighted'), ('info_box', 'Info Box'), ('icon_list', 'Icon List'), ('video', 'Video'), ('audio', 'Audio'), ('video_embed', 'Video Embebido'), ('attachment', 'Archivo Adjunto')], max_length=100),
        ),
        migrations.AlterField(
            model_name='layoutmodel',
            name='tittle',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]